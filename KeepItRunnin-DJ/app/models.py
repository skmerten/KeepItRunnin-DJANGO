"""
Definition of models.
"""

from django.db import models

class Vehicle(models.Model):
    year = models.IntegerField(max_length=None)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)
    mileage = models.IntegerField(max_length=None)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.year) + ' - ' + self.make + ' - ' + self.model

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    months = models.IntegerField(max_length=None)
    miles = models.IntegerField(max_length=None)
    materials = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)

    def __str__(self):
        return str(self.pk) + ' ' + self.vehicle.make + ' ' + self.vehicle.model + ' ' +  self.item + ' ' + self.action

class Maintenance_History(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    comments = models.CharField(max_length=250)
    date_completed = models.DateTimeField()
    next_due_date = models.DateTimeField()
    next_due_mile = models.IntegerField(max_length=None)
    completed = models.IntegerField(max_length=None)

    def __str__(self):
        return self.item + ' ' + self.action + ' ' + self.date_completed

class Part(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    maintenance = models.ForeignKey(Maintenance, on_delete=None)
    part_name = models.CharField(max_length=250)
    date_requested = models.DateTimeField(auto_now_add=True)
    need_by_date = models.DateTimeField()
    purchase_location = models.CharField(max_length=250)
    purchase_price = models.CharField(max_length=50)
    date_of_purchase = models.DateTimeField()
    comments = models.CharField(max_length=250)
    status = models.IntegerField(max_length=None)

    def __str__(self):
        return self.part_name
