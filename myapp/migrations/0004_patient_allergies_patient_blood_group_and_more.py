# Generated by Django 5.2.1 on 2025-05-16 05:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_patient_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_group',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField(unique=True)),
                ('consultation_fee', models.BigIntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
