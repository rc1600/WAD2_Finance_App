from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect 
from django.urls import reverse 
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Save the new user to the database
            login(request, user) # Log the user in
            return redirect(reverse('home')) # Redirect to home page (will change depending on what we call the home page)
        
    else:
        form = UserCreationForm() # If not a post request, create an empty from

    return render(request, 'signup.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')