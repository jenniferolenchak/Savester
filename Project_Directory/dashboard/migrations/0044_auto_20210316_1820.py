# Generated by Django 3.1.6 on 2021-03-16 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0043_auto_20210316_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='age',
            field=models.IntegerField(blank=True, default=20),
        ),
    ]
