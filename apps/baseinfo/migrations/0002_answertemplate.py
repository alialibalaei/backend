# Generated by Django 4.1.1 on 2022-09-21 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('value', models.PositiveSmallIntegerField()),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinfo.metric')),
            ],
        ),
    ]
