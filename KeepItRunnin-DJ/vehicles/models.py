from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    # General
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255, blank=True, null=True)

    # Vehicle General
    year = models.IntegerField(max_length=None)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    vehicle_creation = models.DateTimeField(auto_now_add=True)

    # Vehicle Details
    tankSize = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    mileage = models.IntegerField(max_length=None)
    transmission = models.CharField(max_length=100, blank=True, null=True)
    driveWheels = models.CharField(max_length=100, blank=True, null=True)

    # Vehicle Stats
    mpg = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.year) + ' - ' + self.make + ' - ' + self.model
