# Generated by Django 3.1.6 on 2021-03-06 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0008_auto_20210306_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentlist',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='auth.user'),
            preserve_default=False,
        ),
    ]
