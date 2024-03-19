# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + ", " + \
            "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    MICRO = 'Micro'
    SEDAN = 'Sedan'
    CUV ='CUV'
    SUV = 'SUV'
    HATCHBACK = 'Hatchback'
    ROADSTER = 'Roadster'
    PICKUP = 'Pickup'
    VAN = 'Van'
    COUPE = 'Coupe'
    SUPERCAR = 'Supercar'
    CAMPERVAN = 'Campervan'
    MINITRUCK = 'Mini Truck'
    CABRIOLET = 'Cabriolet'
    MINIVAN = 'Minivan'
    TRUCK = 'Truck'
    BIGTRUCK = 'Big Truck'
    WAGON = 'Wagon'
    CAR_TYPE = [
        (MICRO, 'Micro'),
        (SEDAN, 'Sedan'),
        (CUV,'CUV'),
        (SUV, 'SUV'),
        (HATCHBACK,'Hatchback'),
        (ROADSTER,'Roadster'),
        (PICKUP,'Pickup'),
        (VAN,'Van'),
        (COUPE,'Coupe'),
        (SUPERCAR,'Supercar'),
        (CAMPERVAN,'Campervan'),
        (MINITRUCK,'Mini Truck'),
        (CABRIOLET,'Cabriolet'),
        (MINIVAN,'Minivan'),
        (TRUCK,'Truck'),
        (BIGTRUCK,'Big Truck'),
        (WAGON, 'Wagon')
    ]
    maker = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealerid = models.IntegerField(default=0)
    name = models.CharField(null=False, max_length=30)
    modeltype = models.CharField(max_length=10, choices=CAR_TYPE, default=SEDAN)
    engine = models.CharField(max_length=30)
    year = models.IntegerField(default=0)

    def __str__(self):
        return "Name: " + self.name + ", " + \
            "Type: " + self.modeltype + ", " + \
            "Engine: " + self.engine + ", " + \
            "Year: " + self.year
