"""finance_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name ='signup'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', home_view, name='home'),  # Map the root URL to the home_view
    path('', views.index, name='index'),  
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'),  
    path('contact_us/', views.contact_us, name='contact_us'),  
    path('about/', views.about, name='about'), 
    path('user_account/', views.user_account, name='user_account'),
    path('financial_account/', views.financial_account, name='financial_account'),  
    path('add_new_account/', views.add_new_account, name='add_new_account'),  
    path('budget/', views.budget, name='budget'),  
    path('income_expenditure/', views.income_expenditure, name='income_expenditure'),  
    path('analytics/', views.analytics, name='analytics'), 
]
