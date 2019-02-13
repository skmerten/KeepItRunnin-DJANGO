from django.db import models
from maintenance.models import Maintenance

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