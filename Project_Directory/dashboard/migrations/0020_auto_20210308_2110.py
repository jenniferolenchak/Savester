# Generated by Django 3.1.6 on 2021-03-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20210308_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='paymentOrIncome',
            field=models.CharField(choices=[('Payment', 'Payment'), ('Income', 'Income')], default='payment', max_length=26, null=True),
        ),
    ]