"""
Definition of models.
"""

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
    #picture = models.ImageField(upload_to='static/app/imgs/')
    vehicle_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.year) + ' - ' + self.make + ' - ' + self.model

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
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

class Part(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    part_name = models.CharField(max_length=250)
    part_description = models.CharField(max_length=250,null=True)
    quantity = models.IntegerField(max_length=None)
    date_requested = models.DateTimeField(auto_now_add=True)
    need_by_date = models.DateTimeField(null=True)
    comments = models.CharField(max_length=250,null=True)
    status = models.BooleanField()

    def __str__(self):
        return self.part_name


class Part_History(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    purchase_location = models.CharField(max_length=250,null=True)
    purchase_price = models.CharField(max_length=50,null=True)
    date_of_purchase = models.DateTimeField(null=True)
    after_comments = models.CharField(max_length=250,null=True)
    
    def __str__(self):
        return self.part.part_name + ' ' + "History"
