from ast import Delete
from django.db import models

# Create your models here.

class BikeType(models.Model):
    description_type = models.CharField(max_length=20, blank=True, default='')

class Brands(models.Model):
    description_brand = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

class Bike(models.Model):
    bike_type = models.ForeignKey(BikeType, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    cylinder_capacity = models.FloatField()
    model = models.CharField(max_length=20, blank=True, default='')
    reference = models.CharField(max_length=20, blank=True, default='')
    year = models.IntegerField(blank=True)
    enrollment_year = models.IntegerField(blank=True)
    color = models.CharField(max_length=20, blank=True, default='sin color')
    licence_plate = models.CharField(max_length=10)
    serial_engine = models.CharField(max_length=100)
    serial_chasis = models.CharField(max_length=100)
    