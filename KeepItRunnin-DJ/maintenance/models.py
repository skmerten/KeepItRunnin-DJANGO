from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=100,null=True)
    months = models.IntegerField(max_length=None)
    miles = models.IntegerField(max_length=None)
    materials = models.CharField(max_length=250,null=True)
    comments = models.CharField(max_length=250,null=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.vehicle.make + ' ' + self.vehicle.model + ' ' +  self.name

class Maintenance_History(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    comments = models.CharField(max_length=250)
    date_completed = models.DateTimeField()
    current_mileage = models.IntegerField(max_length=None)
    next_due_date = models.DateTimeField()
    next_due_mile = models.IntegerField(max_length=None)
    completed = models.IntegerField(max_length=None)

    def __str__(self):
        return self.maintenance.name + ' ' + self.maintenance.description + ' ' + 'due'

class ExamplePlans(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,null=True)
    months = models.IntegerField(max_length=None)
    miles = models.IntegerField(max_length=None)
    materials = models.CharField(max_length=250,null=True)
    comments = models.CharField(max_length=250,null=True)


class OilChange(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    oilType = models.CharField(max_length=200,null=False)
    oilBrand = models.CharField(max_length=200,null=False)
    oilQuantity = models.DecimalField(null=False)
    oilUnit = models.CharField(max_length=200,null=False)
    filterSize = models.CharField(max_length=200,null=False)
    filterBrand = models.CharField(max_length=200,null=False)
    drnBltSize = models.CharField(max_length=200,null=False)
    drnBltWasherType = models.CharField(max_length=200,null=False)
    drnBltWasherSize = models.DecimalField(null=False)
    gloves = models.BooleanField(UnboundLocalError=False)

    def __str__(self):
        return self.vehicle + ' Oil Change'