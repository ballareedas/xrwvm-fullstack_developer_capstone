from django.contrib import admin
from .models import CarMake, CarModel, Review

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Review)

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
