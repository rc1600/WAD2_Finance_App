from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages  # Import messages
from .forms import CustomUserCreationForm
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

def signup(request):
    return render(request, 'signUp.html')

def login_view(request):  # Use this function as the login view
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # Use the aliased auth_login
            return redirect(reverse('userAccountPage'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def create_graph(request):
    static_dir = settings.STATICFILES_DIRS[1]  # Get the first directory in STATICFILES_DIRS
    image_path = os.path.join(static_dir, 'pie_chart.png')

    if not os.path.exists(image_path):
        sample_data = {'A': {'size': 30, 'color': 'red'},
                       'B': {'size': 40, 'color': 'blue'},
                       'C': {'size': 20, 'color': 'green'},
                       'D': {'size': 10, 'color': 'yellow'}}

        labels = sample_data.keys()
        sizes = [node_data['size'] for node_data in sample_data.values()]
        colors = [node_data['color'] for node_data in sample_data.values()]

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')

        plt.savefig(image_path)
        plt.close()

    return image_path


def contactUs(request):
    return render(request, 'contactUs.html')

def about(request):
    return render(request, 'aboutUs.html')

def userAccountPage(request):
    userProfile = UserProfile.objects.all()
    print(len(userProfile))
    #userProfile =  UserProfile.objects.get(user = request.user)
    #bank_accounts = FinancialAccount.objects.filter(username=request.user)
    return render(request, 'userAccountPage.html', {'bank_accounts': userProfile})

def financialAccount(request):
    return render(request, 'financialAccount.html')

def newAccount(request):
    return render(request, 'newAccount.html')

def budget(request):
    return render(request, 'budget.html')

def incomeOutcome(request):
    return render(request, 'incomeOutcome.html')

def analysis(request):
    return render(request, 'analysis.html')