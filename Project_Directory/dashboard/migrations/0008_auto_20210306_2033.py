# Generated by Django 3.1.6 on 2021-03-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210306_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentlist',
            name='user',
        ),
        migrations.AlterField(
            model_name='paymentlist',
            name='name',
            field=models.CharField(max_length=26, null=True),
        ),
    ]
