# Generated by Django 4.1.1 on 2022-10-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0011_alter_metricimpact_metric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='title',
            field=models.TextField(),
        ),
    ]
