# Generated by Django 5.1.3 on 2024-12-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type', models.CharField(choices=[('Appetizer', 'Appetizer'), ('Main Course', 'Main Course'), ('Dessert', 'Dessert')], max_length=50)),
                ('cuisine', models.CharField(max_length=100)),
            ],
        ),
    ]
