# Generated by Django 4.1.1 on 2022-09-20 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_space_useraccess_space_users_user_default_space'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='space',
            name='last_modification_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='space',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='space',
            name='users',
            field=models.ManyToManyField(related_name='spaces', through='account.UserAccess', to=settings.AUTH_USER_MODEL),
        ),
    ]
