# Generated by Django 2.2.28 on 2024-03-21 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='budget',
            unique_together={('date', 'financial_account', 'category')},
        ),
        migrations.AlterUniqueTogether(
            name='expense',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='income',
            unique_together={('date', 'financial_account', 'source')},
        ),
    ]
