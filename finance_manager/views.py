from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages
from .forms import CustomUserCreationForm, FinancialAccountForm, ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login  # Alias the login function
import os
from .models import FinancialAccount, UserProfile, ContactMessage
#import matplotlib.pyplot as plt
from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import HttpResponse
import io
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render
import plotly.graph_objs as go
from .models import Expense



def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            if user is not None and user.is_active:
                login(request, user)  # Log the user in
                return redirect(reverse('userAccountPage'))  # Redirect to home page
            else:
                # User might not be active, or authentication backend is not returning the user
                messages.error(request, "Account created successfully, please verify your email before login.")
        else:
            print(form.errors)
            messages.error(request, "There was a problem with the registration. Please try again.")
    else:
        form = CustomUserCreationForm()  # If not a post request, create an empty form

    return render(request, 'signup.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')
    

def login_view(request):  # Use this function as the login view
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # Use the aliased auth_login
            return redirect(reverse('userAccountPage'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def analysis_view(request):
    expenses = Expense.objects.all()
    labels = [expense.product_name for expense in expenses]
    values = [expense.price for expense in expenses]

    trace = go.Pie(labels=labels, values=values)

    layout = go.Layout(title='Expense Analysis')

    fig = go.Figure(data=[trace], layout=layout)

    plot_div = fig.to_html(full_html=False)

    return render(request, 'analysis.html', {'plot_div': plot_div})

def contactUs(request):
    return render(request, 'contactUs.html')

def newSpending(request):
    return render(request, 'newSpending.html')

def incomeOutcome(request):
    if request.method == 'POST':
        return redirect('newSpending')
    else:
        return render(request, "incomeOutcome.html")
    
def about(request):
    return render(request, 'aboutUs.html')

@login_required
def userAccountPage(request):
    try:
        userProfile =  UserProfile.objects.get(user = request.user)
        bank_accounts = FinancialAccount.objects.filter(username = userProfile)
    except ():
        print("User not logged in")

    return render(request, 'userAccountPage.html', {'bank_accounts': bank_accounts})

def financialAccount(request, account_slug):
    context_dict = {}
    try:
        context_dict['financial_account'] = account_slug
    except:
        context_dict['financial_account'] = None
    return render(request, 'financialAccount.html', context_dict)

def newAccount(request):
    if request.method == 'POST':
        form = FinancialAccountForm(request.POST, request.FILES)
        if form.is_valid():
            userProfile =  UserProfile.objects.get(user = request.user)
            form.save(userProfile)
            redirect(reverse('userAccountPage'))
        else:
            print(form.errors)
            messages.error(request, "There was a problem creating a new account. Please try again.")
    else:
        form = FinancialAccountForm()  # If not a post request, create an empty form
    return render(request, 'newAccount.html', {"form":form})

def budget(request):
    return render(request, 'budget.html')

def incomeOutcome(request):
    return render(request, 'incomeOutcome.html')

from .models import ContactMessage

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
