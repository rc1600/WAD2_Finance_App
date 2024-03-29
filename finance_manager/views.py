from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, FinancialAccountForm, ContactForm, BudgetForm, NewSpendingForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login  # Alias the login function
from .models import FinancialAccount, UserProfile, ContactMessage, Budget, Expense, NewSpending
from django.shortcuts import render
import plotly.graph_objs as go
from .models import ContactMessage


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("We made it here")
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('userAccountPage')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('userAccountPage')  
            else:
                form.add_error(None, "Username or password is incorrect")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def analysis_view(request, account_slug):
    account = getAccount(request, account_slug)

    # Retrieve both Expenses and NewSpendings for the account
    expenses = Expense.objects.filter(financial_account=account)
    new_spendings = NewSpending.objects.filter(financial_account=account)

    # Combine the two types of spending into a single list of tuples (category, amount)
    combined_spendings = [(expense.category, expense.price) for expense in expenses]
    combined_spendings.extend([(spending.category, spending.amount) for spending in new_spendings])

    if not combined_spendings:
        return render(request, 'analysis.html', {'plot_div': "THERE ARE NO EXPENSES CURRENTLY"})

    # Use a dictionary to sum amounts by category
    category_totals = {}
    for category, amount in combined_spendings:
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    
    labels = list(category_totals.keys())
    values = list(category_totals.values())

    trace = go.Pie(labels=labels, values=values)
    layout = go.Layout(title='Expense Analysis')
    fig = go.Figure(data=[trace], layout=layout)
    plot_div = fig.to_html(full_html=False)

    return render(request, 'analysis.html', {'plot_div': plot_div})


def contactUs(request):
    return render(request, 'contactUs.html')

def newSpending(request, account_slug):
    if request.method == 'POST':
        form = NewSpendingForm(request.POST, request.FILES)
        if form.is_valid():
            account = getAccount(request, account_slug)
            form.save(account)
            print(account_slug)
            return redirect(reverse('incomeOutcome', kwargs={'account_slug':account_slug}))
        else:
            print(form.errors)
            messages.error(request, "There was a problem adding your spending. Please try again.")
    else:
        form = NewSpendingForm()  # If not a post request, create an empty form
    return render(request, 'newSpending.html', {"form" : form})

    
def about(request):
    return render(request, 'aboutUs.html')

@login_required
def userAccountPage(request):

    userProfile =  UserProfile.objects.get(user = request.user)
    bank_accounts = FinancialAccount.objects.filter(username = userProfile)
    return render(request, 'userAccountPage.html', {'bank_accounts': bank_accounts})

def financialAccount(request, account_slug):
    account = getAccount(request, account_slug)
    context_dict = {}
    try:
        context_dict['financial_account'] = account
    except:
        context_dict['financial_account'] = None
    return render(request, 'financialAccount.html', context_dict)

def newAccount(request):

    MAX_ACCOUNTS_PER_USER = 3

    if request.method == 'POST':
        form = FinancialAccountForm(request.POST, request.FILES)
        if form.is_valid():
            userProfile =  UserProfile.objects.get(user = request.user)
            form.save(userProfile)
            return redirect(reverse('userAccountPage'))
        else:
            print(form.errors)
            messages.error(request, "There was a problem creating a new account. Please try again.")
    else:
        form = FinancialAccountForm()
    return render(request, 'newAccount.html', {"form":form})

def budget(request, account_slug):
    account = getAccount(request, account_slug)
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save(account)
            return redirect(reverse('budget', kwargs={'account_slug':account_slug}))
    else:
        form = BudgetForm()

    existing_budget = Budget.objects.filter(financial_account = account)

    return render(request, 'budget.html', {'form': form, 'existing_budget': existing_budget, 'account_slug':account_slug})

def incomeOutcome(request, account_slug):
    if request.method == 'POST':
        return redirect('newSpending')
    account = getAccount(request, account_slug)
    print(account)
    spending = NewSpending.objects.filter(financial_account=account)
    print(len(spending))
    return render(request, 'incomeOutcome.html', {'financial_account':account,'bank_statements':spending})

def contact_form_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Thank you for your message! We will get back to you soon.")
            return redirect('contact_us')  
    else:
        form = ContactForm()

    return render(request, 'ContactUs.html', {'form': form})

def deleteBudget(request, id, account_slug):
    to_delete = Budget.objects.get(id=id)
    to_delete.delete()
    return redirect(reverse('budget', kwargs={'account_slug':account_slug}))

def deleteFinancialAccount(request, account_slug):
    account = getAccount(request, account_slug)
    to_delete = account
    to_delete.delete()
    return redirect(reverse('userAccountPage'))

def getAccount(request, account_slug):
    userProfile =  UserProfile.objects.get(user = request.user)
    account = FinancialAccount.objects.get(username = userProfile, slug = account_slug)
    return account
