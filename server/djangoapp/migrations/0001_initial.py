# Generated by Django 5.2.3 on 2025-07-02 08:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('founded_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('car_type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Wagon', 'Wagon'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Truck', 'Truck')], default='Sedan', max_length=20)),
                ('year', models.IntegerField(default=2023, validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(2015)])),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='djangoapp.carmake')),
            ],
        ),
    ]
