# Generated by Django 4.1.1 on 2022-09-27 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0008_alter_answertemplate_metric'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metricimpact',
            old_name='value',
            new_name='level',
        ),
    ]