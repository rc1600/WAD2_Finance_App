# Generated by Django 4.2.9 on 2024-03-22 18:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import finance_manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
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
                ('picture', models.ImageField(upload_to=finance_manager.models.user_dir_path)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewSpending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('Rent', 'Rent'), ('Electric bill', 'Electric Bills'), ('Water bill', 'Water Bills'), ('Groceries', 'Groceries'), ('Assets', 'Assets'), ('Cleanliness', 'Cleanliness'), ('Intenet', 'Internet'), ('Transportation', 'Transportation'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], max_length=128)),
                ('amount', models.IntegerField()),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.financialaccount')),
            ],
        ),
        migrations.AddField(
            model_name='financialaccount',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.userprofile'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('category', models.CharField(choices=[('Rent', 'Rent'), ('Electric bill', 'Electric Bills'), ('Water bill', 'Water Bills'), ('Groceries', 'Groceries'), ('Assets', 'Assets'), ('Cleanliness', 'Cleanliness'), ('Intenet', 'Internet'), ('Transportation', 'Transportation'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], max_length=128)),
                ('product_name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.financialaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('Rent', 'Rent'), ('Electric bill', 'Electric Bills'), ('Water bill', 'Water Bills'), ('Groceries', 'Groceries'), ('Assets', 'Assets'), ('Cleanliness', 'Cleanliness'), ('Intenet', 'Internet'), ('Transportation', 'Transportation'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], max_length=128)),
                ('amount', models.FloatField()),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.financialaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('source', models.CharField(max_length=128)),
                ('amount', models.FloatField()),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_manager.financialaccount')),
            ],
            options={
                'unique_together': {('date', 'financial_account', 'source')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='financialaccount',
            unique_together={('username', 'financial_account_id')},
        ),
    ]
