from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from finance_manager.categories import CATEGORIES
from django.db import models
from django.core.validators import MinValueValidator

class UserProfile(models.Model):
    NAME_MAX_LENGTH = 128
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super(UserProfile, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.user.username

class FinancialAccount(models.Model):
    NAME_MAX_LENGTH = 128
    
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    financial_account_id = models.AutoField(primary_key=True)
    financial_account_name = models.CharField(max_length=NAME_MAX_LENGTH)
    savings_balance = models.FloatField(validators=[MinValueValidator(0)])
    current_balance = models.FloatField(validators=[MinValueValidator(0)])
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.financial_account_name)
        super(FinancialAccount, self).save(*args,**kwargs)

    class Meta:
        unique_together = ('username', 'financial_account_id')

    def __str__(self):
        return self.financial_account_name

class Budget(models.Model):
    NAME_MAX_LENGTH = 128
    
    financial_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=NAME_MAX_LENGTH, choices=CATEGORIES)
    price = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('date', 'financial_account')

class Income(models.Model):
    NAME_MAX_LENGTH = 128
    
    financial_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE)
    date = models.DateField()
    source = models.CharField(max_length=NAME_MAX_LENGTH)
    amount = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('date', 'financial_account')

class Expense(models.Model):
    NAME_MAX_LENGTH = 128
    
    financial_account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=NAME_MAX_LENGTH, choices=CATEGORIES)
    product_name = models.CharField(max_length=NAME_MAX_LENGTH)
    price = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('date', 'financial_account')