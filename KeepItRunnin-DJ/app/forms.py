"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Vehicle, Maintenance, Maintenance_History, Part, Part_History


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

# Vehicle Class Forms
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

# Maintenance Class Forms
class NewMaintenance(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    vehicle = forms.ModelChoiceField(label='Your Vehicles', queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    name = forms.CharField(label='Name*', required=True, max_length=100, widget=forms.TextInput(attrs={'class' : 'input'}))
    description = forms.CharField(label='Description*', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'input'}))
    months = forms.IntegerField(label='Monthly Interval*', widget=forms.NumberInput(attrs={'class':'input'}))
    miles = forms.IntegerField(label='Mileage Interval*', widget=forms.NumberInput(attrs={'class':'input'}))
    materials = forms.CharField(label='Materials Needed*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    comments = forms.CharField(label='Comments*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    
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

    class Meta:
        model = Maintenance_History
        fields = ('maintenance', 'date_completed', 'current_mileage', 'next_due_date', 'next_due_mile', 'comments', 'completed',  )
        widgets = {
            'next_due_date' : DateInput(),
            'date_completed' : DateInput()
        }



# Parts Class Forms
class NewPart(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    maintenance = forms.ModelChoiceField(label='Maintenance Plans', queryset=Maintenance.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    part_name = forms.CharField(label='Name*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    part_description = forms.CharField(label='Description*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    quantity = forms.IntegerField(label='Quantity Needed', widget=forms.NumberInput(attrs={'class':'input'}))
    need_by_date = forms.DateField(label='Next Due Date', widget=forms.DateInput(attrs={'class':'input'}))
    comments = forms.CharField(label='Comments*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))

    class Meta:
        model = Part
        fields = ('maintenance','part_name','part_description','quantity', 'need_by_date','comments', )


class ChoosePart(forms.ModelForm):
    part = forms.ModelChoiceField(label='Parts', queryset=Part.objects.all(), widget=forms.Select(attrs={'class':'input'}))

    class Meta:
        model = Part
        fields = ('part', )


class NewPartHistory(forms.ModelForm):
    part = forms.ModelChoiceField(label='Your Parts', queryset=Part.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    purchase_location = forms.CharField(label='Purchase Location*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    purchase_price = forms.CharField(label='Purchase Price*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    date_of_purchase = forms.DateField(label='Purchase Date', widget=forms.DateInput(attrs={'class':'input'}))
    comments = forms.CharField(label='Comments*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    status = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Part_History
        fields = ('part', 'purchase_location', 'purchase_price', 'date_of_purchase', 'comments', 'status', )


