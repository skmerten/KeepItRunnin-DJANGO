"""
Definition of models.
"""

from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100)
    active = models.IntegerField(max_length=None)
    year = models.IntegerField(max_length=None)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)
    mileage = models.IntegerField(max_length=None)
    driveable = models.IntegerField(max_length=None)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    check_in = models.IntegerField(max_length=None)
    vehicle_creation = models.DateTimeField(auto_now_add=True)

class Maintenance(models.Model):
    vehicle_id = models.CharField(max_length=100)
    maintenance_id = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    months = models.IntegerField(max_length=None)
    miles = models.IntegerField(max_length=None)
    materials = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)