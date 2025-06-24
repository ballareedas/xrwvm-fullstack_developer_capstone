# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator



class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models
from datetime import date

# Assuming CarMake is already defined in the same or another app
# from .models import CarMake

class CarModel(models.Model):
    # Choices for car type
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    TRUCK = 'Truck'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (TRUCK, 'Truck'),
    ]

    # many to one relationship
    car_make = models.ForeignKey('CarMake', on_delete=models.CASCADE, related_name='models')
    dealer_id = models.IntegerField(null=True,blank=True);
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

