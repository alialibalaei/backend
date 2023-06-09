# Generated by Django 4.1.5 on 2023-05-16 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("baseinfo", "0054_maturitylevel_levelcompetencerelation_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="levelcompetence",
            name="level_competence_relation",
        ),
        migrations.AddField(
            model_name="levelcompetence",
            name="maturity_level_competence",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="baseinfo.maturitylevel",
            ),
        ),
        migrations.AddField(
            model_name="levelcompetence",
            name="value",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name="LevelCompetenceRelation",
        ),
    ]
