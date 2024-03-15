from django.contrib import admin
from finance_manager.models import FinancialAccount
    
class FinancialAccountAdmin(admin.ModelAdmin):
    account_details = []
    
admin.site.register(FinancialAccount, FinancialAccountAdmin)
