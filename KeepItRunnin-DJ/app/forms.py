"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from vehicles.models import Vehicle
from parts.models import Part, Part_History
from maintenance.models import Maintenance, Maintenance_History, ExamplePlans
from feed.models import Post



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

class NewUserForm(forms.ModelForm):
    username = forms.CharField(label='User Name*', max_length=100, required=True, widget=forms.TextInput(attrs={'class' : 'input'}))
    password = forms.CharField(label='Password*', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class' : 'input'}))
    email = forms.EmailField(label='Email Address*', max_length=100, required=True, widget=forms.EmailInput(attrs={'class' : 'input'}))
    first_name = forms.CharField(label='First Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class' : 'input'}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class' : 'input'}))
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', )

# Vehicle Class Forms
class NewVehicle(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    #user = forms.CharField(required=False, widget=forms.HiddenInput())
    year = forms.CharField(label='Year*', max_length=4, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    make = forms.CharField(label='Make', max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    model = forms.CharField(label='Model', max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    trim = forms.CharField(label='Trim', max_length=50, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    mileage = forms.IntegerField(label='Current Mileage', required=False, widget=forms.NumberInput(attrs={'class' : 'input'}))
    image = forms.ImageField(label='Photo Of Vehicle', required=False, widget=forms.ClearableFileInput(attrs={'class' : 'input'}))
        
    class Meta:
        model = Vehicle
        fields = ('year','make','model','trim','mileage','image', )

# Maintenance Class Forms
class NewMaintenance(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    vehicle = forms.ModelChoiceField(label='Your Vehicles', queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    example = forms.ModelChoiceField(label='Templates', queryset=ExamplePlans.objects.all(), widget=forms.Select(attrs={'class':'input'}))
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
        model = Maintenance_History
        fields = ('maintenance', 'date_completed', 'current_mileage', 'next_due_date', 'next_due_mile', 'comments', 'completed', )
        widgets = {
            'next_due_date' : DateInput(),
            'date_completed' : DateInput()
        }



# Parts Class Forms
class NewPart(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    maintenance = forms.ModelChoiceField(label='Maintenance Plans*', required=True, queryset=Maintenance.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    part_name = forms.CharField(label='Name*', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    part_description = forms.CharField(label='Description', required=False, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    quantity = forms.IntegerField(label='Quantity Needed*', required=True, widget=forms.NumberInput(attrs={'class':'input'}))
    need_by_date = forms.DateField(label='Need By Date', required=False, widget=forms.DateInput(attrs={'class':'input'}))
    comments = forms.CharField(label='Comments', required=False, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))
    status = forms.ChoiceField(choices=[('1', 'Already Purchased')], required=False, widget=forms.RadioSelect)

    def __init__(self, user, *args, **kwargs):
        super(NewPart, self).__init__(*args, **kwargs)
        qs = Maintenance.objects.filter(vehicle__user=user)
        self.fields['maintenance'].queryset = qs

    class Meta:
        model = Part
        fields = ('maintenance','part_name','part_description','quantity', 'need_by_date','comments', 'status', )

class PartHistory(forms.ModelForm):
    part = forms.ModelChoiceField(label='Parts*', required=True, queryset=Part.objects.all(), widget=forms.Select(attrs={'class':'input'}))
    purchase_location = forms.CharField(label='Purchase Location', required=False, max_length=250, widget=forms.TextInput(attrs={'class':'input'}))
    purchase_price = forms.FloatField(label = "Purchase Price", required=False, widget=forms.NumberInput(attrs={'class':'input'}))
    date_of_purchase = forms.DateField(label='Date Of Purchase', required=False, widget=forms.DateInput(attrs={'class':'input'}))
    after_comments = forms.CharField(label='Purchase Comments', required=False, max_length=255, widget=forms.TextInput(attrs={'class':'input'}))

    def __init__(self, user, *args, **kwargs):
        super(PartHistory, self).__init__(*args, **kwargs)
        qs = Part.objects.filter(maintenance__vehicle__user=user, status = 0)
        self.fields['part'].queryset = qs

    class Meta:
        model = Part_History
        fields = ('part', 'purchase_location', 'purchase_price', 'date_of_purchase', 'after_comments', )

class ChoosePart(forms.ModelForm):
    part = forms.ModelChoiceField(label='Parts', queryset=Part.objects.all(), widget=forms.Select(attrs={'class':'input'}))

    def __init__(self, user, *args, **kwargs):
        super(ChoosePart, self).__init__(*args, **kwargs)
        qs = Part.objects.filter(maintenance__vehicle__user=user)
        self.fields['part'].queryset = qs

    class Meta:
        model = Part
        fields = ('part', )

class NewPost(forms.ModelForm):
    user = forms.CharField(required=False, widget=forms.HiddenInput())
    content = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'input'}))

    class Meta:
        model = Post
        fields = ('user', 'content',)

class DeleteVehicle(forms.Form):
    vehicles = forms.ModelChoiceField(label='Vehicles', queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class':'input'}))

    def __init__(self, user, *args, **kwargs):
        super(DeleteVehicle, self).__init__(*args, **kwargs)
        qs = Vehicle.objects.filter(user=user)
        self.fields['vehicles'].queryset = qs

    class Meta:
        fields = ('vehicles', )

class ChooseVehicle(forms.ModelForm):
    vehicle = forms.ModelChoiceField(label='Available Vehicles', queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class':'input'}))

    def __init__(self, user, *args, **kwargs):
        super(ChooseVehicle, self).__init__(*args, **kwargs)
        qs = Vehicle.objects.filter(user=user)
        self.fields['vehicle'].queryset = qs

    class Meta:
        model = Vehicle
        fields = ('vehicle', )