"""
Definition of models.
"""

from django.db import models

class Vehicle(models.Model):
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
        return self.item + ' ' + self.action

class Maintenance_History(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    comments = models.CharField(max_length=250)
    date_completed = models.CharField(max_length=100)
    next_due_date = models.CharField(max_length=100)
    next_due_mile = models.IntegerField(max_length=None)
    completed = models.IntegerField(max_length=None)

    def __str__(self):
        return self.item + ' ' + self.action + ' ' + self.date_completed

class Part(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    maintenance = models.ForeignKey(Maintenance)
    part_name = models.CharField(max_length=250)
    date_requested = models.CharField(max_length=50)
    need_by_date = models.CharField(max_length=50)
    purchase_location = models.CharField(max_length=250)
    purchase_price = models.CharField(max_length=50)
    date_of_purchase = models.CharField(max_length=50)
    comments = models.CharField(max_length=250)
    status = models.IntegerField(max_length=None)

    def __str__(self):
        return self.part_name
