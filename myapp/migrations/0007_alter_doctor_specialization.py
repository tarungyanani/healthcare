# Generated by Django 5.2.1 on 2025-05-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_doctor_consultation_fee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
