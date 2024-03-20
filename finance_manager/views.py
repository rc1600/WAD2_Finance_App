from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages
from .forms import CustomUserCreationForm, FinancialAccountForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login  # Alias the login function
import os
from .models import FinancialAccount, UserProfile
import matplotlib.pyplot as plt
from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import HttpResponse


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

from django.shortcuts import render

def analysis(request):
    # Dummy data (replace this with your data retrieval logic)
    data = {
        'labels': ["January", "February", "March", "April", "May", "June", "July"],
        'values': [65, 59, 80, 81, 56, 55, 40]
    }
    return render(request, 'analysis.html', context=data)



def contactUs(request):
    return render(request, 'contactUs.html')

def about(request):
    return render(request, 'aboutUs.html')

@login_required
def userAccountPage(request):
    userProfile =  UserProfile.objects.get(user = request.user)
    bank_accounts = FinancialAccount.objects.filter(username = userProfile)
    return render(request, 'userAccountPage.html', {'bank_accounts': bank_accounts})

def financialAccount(request):
    return render(request, 'financialAccount.html')

def newAccount(request):
    if request.method == 'POST':
        form = FinancialAccountForm(request.POST)
        if form.is_valid():
            userProfile =  UserProfile.objects.get(user = request.user)
            form.save(userProfile)  # Save the new user to the database
            redirect(reverse('userAccountPage'))
        else:
            print(form.errors)
            messages.error(request, "There was a problem with the registration. Please try again.")
    else:
        form = FinancialAccountForm()  # If not a post request, create an empty form
    return render(request, 'newAccount.html', {"form":form})

def budget(request):
    return render(request, 'budget.html')

def incomeOutcome(request):
    return render(request, 'incomeOutcome.html')

def analysis(request):
    return render(request, 'analysis.html')