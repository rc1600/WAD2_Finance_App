from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages  # Import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login  # Alias the login function
import pydot
from django.http import HttpResponse


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
            return redirect(reverse('home'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def create_graph(request):
    sample_data = {'A': {'size': 30, 'color': 'red'},
                   'B': {'size': 40, 'color': 'blue'},
                   'C': {'size': 20, 'color': 'green'},
                   'D': {'size': 10, 'color': 'yellow'}}

    graph = pydot.Dot(graph_type='graph')

    for label, node_data in sample_data.items():
        node = pydot.Node(label, shape='circle', width=str(node_data['size']), style='filled', fillcolor=node_data['color'])
        graph.add_node(node)

    image_data = graph.create_png(prog='circo')

    return HttpResponse(image_data, content_type='image/png')

def contactUs(request):
    return render(request, 'contactUs.html')

def about(request):
    return render(request, 'aboutUs.html')

def userAccountPage(request):
    return render(request, 'userAccountPage.html')

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