import os
from datetime import datetime
from django.contrib.auth.models import User
from finance_manager.categories import RENT, ELECTRIC_BILL, WATER_BILL, GROCERIES, ASSETS, CLEANLINESS, INTERNET, TRANSPORTATION, ENTERTAINMENT, OTHERS

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'finance_manager.settings')

import django
django.setup()
from finance_manager.models import UserProfile, FinancialAccount, Budget, Income, Expense

def populate():
    # Lists of dictionaries for each model
    # Note that these models are built for optimum insertion. The true model
    #     structure can be found in models.py
    # Eg: The are no fields in FinancialAccount model thats stores a list of
    #     all budget entries. This is only to smoothly enter the budget in a
    #     single nested-for-loop.
    
    user_profile_list = [{'username':'Bob', 'email':'bob@gmail.com', 'password':'Bob'},] #just one user profile
    
    # fin_acc_dict = {<fin_acc_name>:{'financial_account_name': str, 'savings_balance': float
    #                                   'current_balance': float},...}
    financial_account_list = [{'financial_account_name': 'Bob', 'savings_balance': 150,
                                'current_balance': 0},]

    # budget = [{'date':datetime(Y,M,D),'category':str,'amount':float},...]
    budget_list = [{'date': datetime(2024,1,1).date(), 'category': RENT, 'amount': 500},
                   {'date': datetime(2024,1,1).date(), 'category': GROCERIES, 'amount': 100},
                   {'date': datetime(2024,1,1).date(), 'category': ASSETS, 'amount': 50},
                   {'date': datetime(2024,1,1).date(), 'category': INTERNET, 'amount': 20},
                   {'date': datetime(2024,1,1).date(), 'category': CLEANLINESS, 'amount': 10},
                   {'date': datetime(2024,2,1).date(), 'category': RENT, 'amount': 500},
                   {'date': datetime(2024,2,1).date(), 'category': GROCERIES, 'amount': 100},
                   {'date': datetime(2024,2,1).date(), 'category': ASSETS, 'amount': 50},
                   {'date': datetime(2024,2,1).date(), 'category': INTERNET, 'amount': 20},
                   {'date': datetime(2024,2,1).date(), 'category': CLEANLINESS, 'amount': 10},
                   ]
    
    
    # income = [{'date':datetime(Y,M,D),'source':str,'amount':float},...]
    income_list = [{'date':datetime(2024,1,1).date(),'source':'Sponsorship','amount':1100},
                   {'date':datetime(2024,2,1).date(),'source':'Sponsorship','amount':1100},
                   ]
    
    # expense = [{'date':datetime(Y,M,D),'category':str,'product_name':str,'price':float},...]
    expense_list = [{'date':datetime(2024,1,3).date(),'category':RENT,'product_name':RENT, 'price':500},
                    {'date':datetime(2024,1,4).date(),'category':GROCERIES,'product_name':'Basmati Rice, Bread, Cheese','price':17.50},
                    {'date':datetime(2024,1,5).date(),'category':GROCERIES,'product_name':'Apple pack, Cocoa Powder','price':6.00},
                    {'date':datetime(2024,1,6).date(),'category':INTERNET,'product_name':'VOXI Plan','price':12.00},
                    {'date':datetime(2024,1,7).date(),'category':CLEANLINESS,'product_name':'Sponge Pack x6','price':2.99},
                    {'date':datetime(2024,2,3).date(),'category':RENT,'product_name':RENT,'price':500},
                    {'date':datetime(2024,2,4).date(),'category':GROCERIES,'product_name':'Bread, butter, garlic','price':6.00},
                    {'date':datetime(2024,2,5).date(),'category':GROCERIES,'product_name': 'Coconut, Pizza Dough,','price':10.99},
                    {'date':datetime(2024,2,6).date(),'category':ASSETS,'product_name':'Phone Charger','price':8.99},
                    {'date':datetime(2024,2,7).date(),'category':INTERNET,'product_name':'VOXI Plan','price':12.00},
                    ]
    
    #date = datetime.date()
    #month = date.month
    
    # Insert For-Loop for data insertion
    for data in user_profile_list:
        add_user_profile(data)
        for fin_acc in financial_account_list:
            this_fin_acc = add_fin_acc(data['username'], fin_acc['financial_account_name'], fin_acc['savings_balance'], fin_acc['current_balance'])
            for budget in budget_list:
                add_budget(this_fin_acc, budget['date'], budget['category'], budget['amount'])
            for income in income_list:
                add_income(this_fin_acc, income['date'], income['source'], income['amont'])
            for expense in expense_list:
                add_expense(this_fin_acc, expense['date'], expense['category'], expense['product_name'], expense['price'])
    
    # Print out added data

def add_user_profile(data):
        user = User.objects.create(username=data['username'], email=data['email'], password=data['password'])
        UserProfile.objects.get_or_create(user=user)

def add_fin_acc(username, financial_account_name, savings_balance,current_balance=0):
    fin_acc = FinancialAccount.objects.get_or_create(username=username, financial_account_name=financial_account_name)[0]
    fin_acc.savings_balance=savings_balance
    fin_acc.current_balance=current_balance
    fin_acc.save()
    return fin_acc

def add_budget(financial_account, date, category, amount):
    budget = Budget.objects.get_or_create(financial_account=financial_account)[0]
    budget.date=date
    budget.category=category
    budget.amount=amount
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