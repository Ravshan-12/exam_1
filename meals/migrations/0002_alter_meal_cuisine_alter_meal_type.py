# Generated by Django 5.1.3 on 2024-12-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='cuisine',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='meal',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
