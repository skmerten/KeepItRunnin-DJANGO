"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Vehicle, Maintenance


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class NewVehicle(forms.ModelForm):
    year = forms.CharField(label='Year*', max_length=4, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    make = forms.CharField(label='Make', max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    model = forms.CharField(label='Model', max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    trim = forms.CharField(label='Trim', max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    mileage = forms.IntegerField(label='Current Mileage', widget=forms.NumberInput(attrs={'class' : 'input'}))
    email = forms.EmailField(label='Notification Email Address', required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    phone = forms.CharField(label='Notification Phone Number', max_length=20, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))

    class Meta:
        model = Vehicle
        fields = ('year','make','model','trim','mileage','email','phone', )

class NewMaintenance(forms.ModelForm):
    vehicle = forms.ModelChoiceField(label='Your Vehicles', queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    item = forms.CharField(label='Item*', required=True, max_length=100, widget=forms.TextInput(attrs={'class' : 'input'}))
    action = forms.CharField(label='Action*', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'input'}))
    months = forms.IntegerField(label='Monthly Interval*', widget=forms.NumberInput(attrs={'class':'input'}))
    miles = forms.IntegerField(label='Mileage Interval*', widget=forms.NumberInput(attrs={'class':'input'}))
    materials = forms.CharField(label='Materials Needed*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    comments = forms.CharField(label='Comments*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    
    class Meta:
        model = Maintenance
        fields = ('vehicle', 'item', 'action', 'months', 'miles', 'materials', 'comments',)

class ChooseMaintenance(forms.ModelForm):
    maintenance = forms.ModelChoiceField(label='Maintenance Plans', queryset=Maintenance.objects.all(), widget=forms.Select(attrs={'class':'input'}))

    class Meta:
        model = Maintenance
        fields = ('maintenance', )
#class NewMaintenanceHistory(forms.ModelForm):
#    next_due_date = forms.DateField(label='Next Due Date', widget=forms.DateInput(attrs={'class':'input'}))
#    next_due_mile = forms.IntegerField(label='Next Due Mileage', widget=forms.NumberInput(attrs={'class':'input'}))