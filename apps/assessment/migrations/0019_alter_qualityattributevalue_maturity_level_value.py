# Generated by Django 4.1.5 on 2023-05-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assessment", "0018_assessmentproject_maturity_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qualityattributevalue",
            name="maturity_level_value",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
