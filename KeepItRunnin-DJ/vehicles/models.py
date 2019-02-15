from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField(max_length=None)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)
    mileage = models.IntegerField(max_length=None)
    image = models.ImageField(blank=True, null=True)
    vehicle_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.year) + ' - ' + self.make + ' - ' + self.model
