import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'finance_manager.settings')

import django
django.setup()
from finance_manager.models import UserProfile, FinancialAccount, Budget, Income, Expense

def populate():
    # lists of dictionaries for each model
    
    user_profiles_list = []
    
    financial_accounts_list = []
    
    budget_list = []
    
    income_list = []
    
    expenses_list = []
    
    pass

def add_user_profile(user_profiles_data):
    for data in user_profiles_data:
        user = UserProfile.objects.create(username=data['username'], email=data['email'], password='password')
        UserProfile.objects.get_or_create(user=user)

def add_fin_acc(username, financial_account_name, savings_balance, current_balance):
    fin_acc = FinancialAccount.objects.get_or_create(username=username, financial_account_name=financial_account_name)[0]
    fin_acc.savings_balance=savings_balance
    fin_acc.current_balance=current_balance
    fin_acc.save()
    return fin_acc

def add_budget(financial_account, date, category, price):
    budget = Budget.objects.get_or_create(financial_account=financial_account)[0]
    budget.date=date
    budget.category=category
    budget.price=price
    budget.save()
    return budget

def add_income(financial_account, date, source, amount):
    income = Income.objects.get_or_create(financial_account=financial_account)[0]
    income.date=date
    income.source=source
    income.amount=amount
    income.save()
    return income

def add_expense(financial_account, date, category, product_name, price):
    expense = Expense.objects.get_or_create(financial_account=financial_account)[0]
    expense.date=date
    expense.category=category
    expense.product_name=product_name
    expense.price=price
    expense.save()
    return expense

if __name__ == '__main__':
    print('Starting Finance Manager population script...')
    populate()