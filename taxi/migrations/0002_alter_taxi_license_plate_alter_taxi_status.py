# Generated by Django 5.1.3 on 2024-12-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxi',
            name='license_plate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
