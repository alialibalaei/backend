# Generated by Django 4.1.1 on 2022-10-15 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_space_creation_time_space_last_modification_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='default_space',
            new_name='current_space',
        ),
    ]
