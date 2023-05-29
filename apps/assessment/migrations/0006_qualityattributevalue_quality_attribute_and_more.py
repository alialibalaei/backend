# Generated by Django 4.1.1 on 2022-09-28 12:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0011_alter_metricimpact_metric'),
        ('assessment', '0005_rename_assessment_results_qualityattributevalue_assessment_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualityattributevalue',
            name='quality_attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quality_attribute_values', to='baseinfo.qualityattribute'),
        ),
        migrations.AddField(
            model_name='qualityattributevalue',
            name='temp_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='qualityattributevalue',
            name='assessment_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quality_attribute_values', to='assessment.assessmentresult'),
        ),
    ]
