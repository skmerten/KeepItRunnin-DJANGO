"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from vehicles.models import Vehicle
from parts.models import Part, Part_History
from maintenance.models import Maintenance, Maintenance_Record, OilChange
from feed.models import Post


# Maintenance Class Forms
class NewMaintenance(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    vehicle = forms.ModelChoiceField(label='Your Vehicles', queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    #vehicle = forms.ModelChoiceField(label='Your Vehicles', widget=forms.Select(attrs={'class':'input'}))
    name = forms.CharField(label='Name*', required=True, max_length=100, widget=forms.TextInput(attrs={'class' : 'input'}))
    description = forms.CharField(label='Description*', required=False, max_length=100, widget=forms.TextInput(attrs={'class':'input'}))
    months = forms.IntegerField(label='Monthly Interval*', widget=forms.NumberInput(attrs={'class':'input'}))
    miles = forms.IntegerField(label='Mileage Interval*', widget=forms.NumberInput(attrs={'class':'input'}))
    materials = forms.CharField(label='Materials Needed*', required=False, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    comments = forms.CharField(label='Comments*', required=False, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
        
    def __init__(self, user, *args, **kwargs):
        super(NewMaintenance, self).__init__(*args, **kwargs)
        qs = Vehicle.objects.filter(user=user)
        self.fields['vehicle'].queryset = qs

    class Meta:
        model = Maintenance
        fields = ('vehicle', 'name', 'description', 'months', 'miles', 'materials', 'comments',)

class ChooseMaintenance(forms.ModelForm):
    maintenance = forms.ModelChoiceField(label='Maintenance Plans', queryset=Maintenance.objects.all(), widget=forms.Select(attrs={'class':'input'}))

    class Meta:
        model = Maintenance
        fields = ('maintenance', )

class DateInput(forms.DateInput):
    input_type = 'date'

class NewMaintenanceHistory(forms.ModelForm):

    maintenance = forms.ModelChoiceField(label='Maintenance Plans', queryset=Maintenance.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    date_completed = forms.DateField(label='Date Completed', widget=forms.DateInput(attrs={'class':'input'}))
    current_mileage = forms.IntegerField(label='Current Mileage', widget=forms.NumberInput(attrs={'class':'input'}))
    next_due_date = forms.DateField(label='Next Due Date', widget=forms.DateInput(attrs={'class':'input'}))
    next_due_mile = forms.IntegerField(label='Next Due Mileage', widget=forms.NumberInput(attrs={'class':'input'}))
    comments = forms.CharField(label='Comments*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    completed = forms.IntegerField(required=False, widget=forms.HiddenInput())

    def __init__(self, user, *args, **kwargs):
        super(NewMaintenanceHistory, self).__init__(*args, **kwargs)
        qs = Maintenance.objects.filter(vehicle__user=user)
        self.fields['maintenance'].queryset = qs

    class Meta:
        model = Maintenance_Record
        fields = ('maintenance', 'date_completed', 'current_mileage', 'next_due_date', 'next_due_mile', 'comments', 'completed', )
        widgets = {
            'next_due_date' : DateInput(),
            'date_completed' : DateInput()
        }

class NewOilChange(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    vehicle = forms.ModelChoiceField(label='Your Vehicles', queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    oilType = forms.CharField(label='Oil Type', required=False, max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    oilBrand = forms.CharField(label='Oil Brand', required=False, max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    oilUnit = forms.CharField(label='Oil Unit', required=False, max_length=100, widget=forms.TextInput(attrs={'class' : 'input'}))
    oilQuantity = forms.DecimalField(label='Quantity of Oil', max_digits = 5, decimal_places=2, widget=forms.NumberInput(attrs={'class':'input'}))
    filterSize = forms.CharField(label='Oil Filter Size', required=False, max_length=100, widget=forms.TextInput(attrs={'class':'input'}))
    filterBrand = forms.IntegerField(label='Oil Filter Brand', widget=forms.NumberInput(attrs={'class':'input'}))
    drnBltSize = forms.IntegerField(label='Drain Bolt Socket Size', widget=forms.NumberInput(attrs={'class':'input'}))
    drnBltWasherType = forms.CharField(label='Drain Bolt Washer Type', required=False, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    drnBltWasherSize = forms.CharField(label='Drain Bolt Washer Size', required=False, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    gloves = forms.BooleanField(label='Do you wear gloves?', required=False, widget=forms.CheckboxInput(attrs={'class':'input'}))

    def __init__(self, user, *args, **kwargs):
        super(NewOilChange, self).__init__(*args, **kwargs)
        qs = Vehicle.objects.filter(user=user)
        self.fields['vehicle'].queryset = qs

    class Meta:
        model = OilChange
        fields = ('vehicle', 'oilType', 'oilBrand', 'oilUnit', 'oilQuantity', 'filterSize', 'filterBrand', 'drnBltSize', 'drnBltWasherType', 'drnBltWasherSize', 'gloves', )