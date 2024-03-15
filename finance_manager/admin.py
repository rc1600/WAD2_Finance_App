from django.contrib import admin
from .models import FinancialAccount, Budget, Income, Expense, UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug')
    prepopulated_fields = {'slug':('user',)}

class FinancialAccountAdmin(admin.ModelAdmin):
    list_display = ('financial_account_name', 'username', 'financial_account_id', 'savings_balance', 'current_balance')
    prepopulated_fields = {'slug':('username','financial_account_name',)}

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('date', 'financial_account', 'category', 'amount')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'financial_account', 'source', 'amount')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'financial_account', 'category', 'product_name', 'price')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(FinancialAccount, FinancialAccountAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
