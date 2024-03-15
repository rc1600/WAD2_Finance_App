from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from .models import UserProfile, Income, Expense, FinancialAccount, Budget

class CustomUserCreationForm(UserCreationForm):  
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.exists():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user']
        exclude = ['slug']
        
class FinancialAccountForm(forms.ModelForm):
    class Meta:
        model = FinancialAccount
        fields = ['username', 'financial_account_name', 'savings_balance', 'current_balance']
        exclude = ['username', 'slug']
        
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['date', 'category', 'amount']
        exclude = ['financial_account']
        
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'source', 'amount']
        exclude = ['financial_account']
        
class ExpenseForm(forms.ModelForm): 
    class Meta:
        model = Expense
        fields = ['date', 'category', 'product_name', 'price']
        exclude = ['financial_account']
        
