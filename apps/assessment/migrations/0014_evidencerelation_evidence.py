# Generated by Django 4.1.7 on 2023-04-10 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0048_alter_answertemplate_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assessment', '0013_alter_assessmentproject_space'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenceRelation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidences', to='assessment.assessmentproject')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidences', to='baseinfo.metric')),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('evidence_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.evidencerelation')),
            ],
        ),
    ]
