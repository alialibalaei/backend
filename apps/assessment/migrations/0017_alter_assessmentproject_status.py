# Generated by Django 4.1.5 on 2023-05-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0016_alter_assessmentproject_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentproject',
            name='status',
            field=models.CharField(choices=[('ELEMENTARY', 'ELEMENTARY'), ('WEAK', 'WEAK'), ('MODERATE', 'MODERATE'), ('GOOD', 'GOOD'), ('GREAT', 'GREAT')], max_length=10, null=True),
        ),
    ]
