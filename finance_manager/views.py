from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages  # Import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            if user is not None and user.is_active:
                login(request, user)  # Log the user in
                return redirect(reverse('home'))  # Redirect to home page
            else:
                # User might not be active, or authentication backend is not returning the user
                messages.error(request, "Account created successfully, please verify your email before login.")
        else:
            messages.error(request, "There was a problem with the registration. Please try again.")
    else:
        form = CustomUserCreationForm()  # If not a post request, create an empty form

    return render(request, 'signup.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'WAD2_FINANCE_APP/signUp.html')

def login(request):
    return render(request, 'WAD2_FINANCE_APP/login.html')

def contact_us(request):
    return render(request, 'WAD2_FINANCE_APP/contactUs.html')

def about(request):
    return render(request, 'WAD2_FINANCE_APP/aboutUs.html')

def user_account(request):
    return render(request, 'WAD2_FINANCE_APP/userAccountPage.html')

def financial_account(request):
    return render(request, 'WAD2_FINANCE_APP/financialAccount.html')

def add_new_account(request):
    return render(request, 'WAD2_FINANCE_APP/newAccount.html')

def budget(request):
    return render(request, 'WAD2_FINANCE_APP/budget.html')

def income_expenditure(request):
    return render(request, 'WAD2_FINANCE_APP/incomeOutcome.html')

def analytics(request):
    return render(request, 'WAD2_FINANCE_APP/analysis.html')