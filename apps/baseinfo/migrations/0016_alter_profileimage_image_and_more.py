# Generated by Django 4.1.1 on 2022-10-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0015_rename_subject_profileimage_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='image',
            field=models.FileField(upload_to='profile/images'),
        ),
        migrations.AlterField(
            model_name='qualityattributeimage',
            name='image',
            field=models.FileField(upload_to='attribute/images'),
        ),
        migrations.AlterField(
            model_name='subjectimage',
            name='image',
            field=models.FileField(upload_to='subject/images'),
        ),
    ]
