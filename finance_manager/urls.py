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
    path('signup/', views.signup_view, name='signup'),  # Only keep one of the signup paths
    # path('signup/', views.signup, name='signup'),  # Remove or rename this path
    path('login/', views.login, name='login'),  # Rename your custom login view URL to avoid clashes
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', home_view, name='home'),
    path('contact-us/', views.contact_us, name='contact_us'),  # Correct the name to match your 'url' tag
    path('about/', views.about, name='about'),
    path('user-account/', views.user_account, name='user_account'),
    path('financial-account/', views.financial_account, name='financial_account'), 
    path('add-new-account/', views.add_new_account, name='add_new_account'),
    path('budget/', views.budget, name='budget'),
    path('income-expenditure/', views.income_expenditure, name='income_expenditure'),
    path('analytics/', views.analytics, name='analytics'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  # Correct the typo
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]

