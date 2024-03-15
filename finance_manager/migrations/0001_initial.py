# Generated by Django 2.2.28 on 2024-03-14 16:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialAccount',
            fields=[
                ('financial_account_id', models.AutoField(primary_key=True, serialize=False)),
                ('financial_account_name', models.CharField(max_length=128)),
                ('savings_balance', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('current_balance', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('slug', models.SlugField(unique=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.CustomUser')),
            ],
            options={
                'unique_together': {('username', 'financial_account_id')},
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('source', models.CharField(max_length=128)),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.FinancialAccount')),
            ],
            options={
                'unique_together': {('date', 'financial_account')},
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('Rent', 'Monthly rent amount'), ('Electric bill', 'Monthly electric bills'), ('Water bill', 'Monthly water bills'), ('Groceries', 'Raw food stuffs for cooking and/or pre-cook, etc.'), ('Assets', 'Long term possessions such as devices, clothing, furniture, etc.'), ('Cleanliness', 'Anything related to cleanliness such as dust bins, plastic bags, etc.'), ('Intenet', 'Mobile service providers subscription'), ('Transportation', 'Public transportation'), ('Entertainment', 'Movies, subcriptions, etc.'), ('Others', 'Any other categories besides of what is described')], max_length=50)),
                ('product_name', models.CharField(max_length=128)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.FinancialAccount')),
            ],
            options={
                'unique_together': {('date', 'financial_account')},
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('Rent', 'Monthly rent amount'), ('Electric bill', 'Monthly electric bills'), ('Water bill', 'Monthly water bills'), ('Groceries', 'Raw food stuffs for cooking and/or pre-cook, etc.'), ('Assets', 'Long term possessions such as devices, clothing, furniture, etc.'), ('Cleanliness', 'Anything related to cleanliness such as dust bins, plastic bags, etc.'), ('Intenet', 'Mobile service providers subscription'), ('Transportation', 'Public transportation'), ('Entertainment', 'Movies, subcriptions, etc.'), ('Others', 'Any other categories besides of what is described')], max_length=50)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.FinancialAccount')),
            ],
            options={
                'unique_together': {('date', 'financial_account')},
            },
        ),
    ]