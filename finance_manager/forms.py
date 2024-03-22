from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from .models import UserProfile, Income, Expense, FinancialAccount, Budget, NewSpending
from finance_manager.categories import CATEGORIES

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your email', 'class':'inputs'}))
    username = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class':'inputs'}))
    password1 = forms.CharField(required=True, max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'inputs'}))
    password2 = forms.CharField(required=True, max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password','class':'inputs'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 10:
            raise ValidationError("Username must be at least 10 characters long")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user']
        exclude = ['slug']
        
class FinancialAccountForm(forms.ModelForm):

    financial_account_name = forms.CharField(required=True, label='Account name', widget=forms.TextInput(attrs={'placeholder': 'Enter the account name', 'class':'inputs'}))
    savings_balance = forms.IntegerField(required=True, label='Savings balance', widget=forms.TextInput(attrs={'placeholder': 'Enter your savings balance', 'class':'inputs'}))
    current_balance = forms.IntegerField(required=True, label='Current balance', widget=forms.TextInput(attrs={'placeholder': 'Enter your current balance', 'class':'inputs'}))
    picture = forms.ImageField(required=True)
    
    #what is the point of these balances

    class Meta:
        model = FinancialAccount
        fields = ['username', 'financial_account_name', 'savings_balance', 'current_balance','picture']
        exclude = ['username']

    def save(self, user, *args, **kwargs):
        self.instance.username = user
        return super().save(*args, **kwargs)
        
class BudgetForm(forms.ModelForm):
    #financial_account_id = forms.
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=True)
    amount = forms.FloatField()
    
    class Meta:
        model = Budget
        fields = '__all__'
        #fields = ['date', 'category', 'amount']
        #exclude = ['financial_account']
        
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

class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message: max length 150 characters', 'cols': 50, 'maxlength': 150, 'class':'contact_message'}))
    
class NewSpendingForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name: ', 'class':'inputs'}))
    category = forms.ChoiceField(required=True, choices=CATEGORIES, widget=forms.Select(attrs={'placeholder': 'Category: ', 'class': 'inputs'}))
    amount = forms.DecimalField(required=True, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Spending amount: ', 'class':'inputs'}))
    
    class Meta:
        model = NewSpending
        fields = ['financial_account', 'category']

