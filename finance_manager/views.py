from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages
from .forms import CustomUserCreationForm, FinancialAccountForm, ContactForm, BudgetForm, NewSpendingForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login  # Alias the login function
from .models import FinancialAccount, UserProfile, ContactMessage, Budget, Expense
from django.shortcuts import render
import plotly.graph_objs as go
from .models import ContactMessage


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            UserProfile.objects.create(user=user)  # Create UserProfile for the new user
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

def analysis_view(request):
    expenses = Expense.objects.all()
    labels = [expense.category for expense in expenses]
    values = [expense.price for expense in expenses]

    trace = go.Pie(labels=labels, values=values)

    layout = go.Layout(title='Expense Analysis')

    fig = go.Figure(data=[trace], layout=layout)

    plot_div = fig.to_html(full_html=False)

    return render(request, 'analysis.html', {'plot_div': plot_div})

def contactUs(request):
    return render(request, 'contactUs.html')

def newSpending(request):
    if request.method == 'POST':
        form = NewSpendingForm(request.POST, request.FILES)
        if form.is_valid():
            userProfile =  UserProfile.objects.get(user = request.user)
            form.save(userProfile)
            return redirect(reverse('incomeOutcome'))
        else:
            print(form.errors)
            messages.error(request, "There was a problem adding your spending. Please try again.")
    else:
        form = NewSpendingForm()  # If not a post request, create an empty form
    return render(request, 'newSpending.html', {"form" : form})

def incomeOutcome(request):
    if request.method == 'POST':
        return redirect('newSpending')
    else:
        return render(request, "incomeOutcome.html")
    
def about(request):
    return render(request, 'aboutUs.html')

@login_required
def userAccountPage(request):

    userProfile =  UserProfile.objects.get(user = request.user)
    bank_accounts = FinancialAccount.objects.filter(username = userProfile)
    return render(request, 'userAccountPage.html', {'bank_accounts': bank_accounts})

def financialAccount(request, account_slug):
    userProfile =  UserProfile.objects.get(user = request.user)
    account = FinancialAccount.objects.get(username = userProfile, slug = account_slug)
    context_dict = {}
    try:
        context_dict['financial_account'] = account.financial_account_name
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
        form = FinancialAccountForm()  # If not a post request, create an empty form
    return render(request, 'newAccount.html', {"form":form})

def budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget')
    else:
        form = BudgetForm()

    existing_budget = Budget.objects.all()

    return render(request, 'budget.html', {'form': form, 'existing_budget': existing_budget})

def incomeOutcome(request):
    return render(request, 'incomeOutcome.html')

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

    return render(request, 'ContactUs.html', {'form': form})  # this needs changed to URL form

def deleteBudget(request, id):
    to_delete = Budget.objects.get(id=id)
    to_delete.delete()
    return redirect('budget')

def deleteFinancialAccount(request, account_slug, financial_account_id):
    to_delete = FinancialAccount.objects.get(financial_account_id=financial_account_id)
    to_delete.delete()
    return redirect('userAccountPage')
