# Generated by Django 3.1.6 on 2021-03-08 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20210308_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='user',
        ),
    ]