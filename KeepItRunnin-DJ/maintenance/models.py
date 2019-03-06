from django.db import models
from datetime import date
from django.contrib.auth.models import User
from vehicles.models import Vehicle

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=100,null=True)
    months = models.DecimalField(max_digits=5, decimal_places=2)
    miles = models.IntegerField(max_length=None)
    materials = models.CharField(max_length=250,null=True)
    comments = models.CharField(max_length=250,null=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.vehicle.make + ' ' + self.vehicle.model + ' ' +  self.name

class Maintenance_Record(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    comments = models.CharField(max_length=250)
    date_completed = models.DateField()
    current_mileage = models.IntegerField(max_length=None)
    next_due_date = models.DateField()
    next_due_mile = models.IntegerField(max_length=None)
    completed = models.IntegerField(max_length=None)

    @property
    def is_past_due(self):
        return date.today() > self.next_due_date
    @property
    def is_due(self):
        return date.today() == self.next_due_date
    @property
    def is_due_soon(self):
        return date.today() < self.next_due_date


    def __str__(self):
        return self.maintenance.name + ' ' + self.maintenance.description + ' ' + 'due'

class OilChange(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    oilType = models.CharField(max_length=200,null=False)
    oilBrand = models.CharField(max_length=200,null=False)
    oilQuantity = models.DecimalField(max_digits = 5, decimal_places=2, null=False)
    oilUnit = models.CharField(max_length=200,null=False)
    filterSize = models.CharField(max_length=200,null=False)
    filterBrand = models.CharField(max_length=200,null=False)
    drnBltSize = models.CharField(max_length=200,null=False)
    drnBltWasherType = models.CharField(max_length=200,null=False)
    drnBltWasherSize = models.CharField(max_length=200,null=False)
    gloves = models.BooleanField(null=False)
    def __str__(self):
        return self.vehicle + ' Oil Change'