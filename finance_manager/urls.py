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
from .views import signup_view
from .views import login_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home_view, name='home'),
    path('contact-us/', views.contactUs, name='contact_us'),
    path('about/', views.about, name='about'),
    path('user-account/', views.userAccountPage, name='userAccountPage'),
    path('financial-account/', views.financialAccount, name='financial_account'),
    path('add-new-account/', views.newAccount, name='newAccount'),
    path('budget/', views.budget, name='budget'),
    path('income-expenditure/', views.incomeOutcome, name='incomeOutcome'),
    path('analysis/', views.analysis, name='analysis'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),  
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('contact/', views.contact_form_submit, name='contact_form_submit'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)