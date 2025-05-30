# Generated by Django 5.2.1 on 2025-05-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_patient_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='consultation_fee',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
