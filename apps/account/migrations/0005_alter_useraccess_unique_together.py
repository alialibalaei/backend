# Generated by Django 4.1.1 on 2022-10-25 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_default_space_user_current_space'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useraccess',
            unique_together={('space', 'user')},
        ),
    ]
