# Generated by Django 4.1.5 on 2023-05-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0015_alter_assessmentproject_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentproject',
            name='status',
            field=models.CharField(choices=[('ElEMENTARY', 'ElEMENTARY'), ('WEAK', 'WEAK'), ('MODERATE', 'MODERATE'), ('GOOD', 'GOOD'), ('GREAT', 'GREAT')], max_length=10, null=True),
        ),
    ]