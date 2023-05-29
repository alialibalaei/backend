# Generated by Django 4.1.5 on 2023-01-30 10:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baseinfo', '0034_expertgroupaccess_alter_expertgroup_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentprofile',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='assessmentprofile',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='assessmentsubject',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        # migrations.AlterField(
        #     model_name='expertgroup',
        #     name='users',
        #     field=models.ManyToManyField(related_name='expert_groups', through='baseinfo.ExpertGroupAccess', to=settings.AUTH_USER_MODEL),
        # ),
        migrations.AlterField(
            model_name='metriccategory',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='profiletag',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='profiletag',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='qualityattribute',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
