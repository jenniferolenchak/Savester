# Generated by Django 3.1.6 on 2021-03-21 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0049_merge_20210319_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='category',
            field=models.CharField(choices=[('Housing', 'Housing'), ('Utilities', 'Utilities'), ('Transportation', 'Transportation'), ('Food/Groceries', 'Food/Groceries'), ('Shopping & Entertainment', 'Shopping & Entertainemnt'), ('Subscriptions', 'Subscriptions'), ('Health', 'Health'), ('Other', 'Other')], default='Food', max_length=26, null=True),
        ),
    ]