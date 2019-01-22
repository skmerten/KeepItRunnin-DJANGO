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
    vehicle_creation = models.DateTimeField(auto_now_add=true)

    def __str__(self):
        return self.vehicle_id