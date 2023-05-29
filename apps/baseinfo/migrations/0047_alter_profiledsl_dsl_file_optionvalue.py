# Generated by Django 4.1.7 on 2023-04-05 14:50

import common.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0046_remove_qualityattributeimage_attribute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledsl',
            name='dsl_file',
            field=models.FileField(upload_to='profile/dsl', validators=[common.validators.validate_file_size]),
        ),
        migrations.CreateModel(
            name='OptionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=3)),
                ('metric_impact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_values', to='baseinfo.metricimpact')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_values', to='baseinfo.answertemplate')),
            ],
        ),
    ]