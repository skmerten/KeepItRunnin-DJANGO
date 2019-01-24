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
    mileage = forms.IntegerField(label='Current Mileage', widget=forms.TextInput(attrs={'class' : 'input'}))
    email = forms.EmailField(label='Notification Email Address', required=False, widget=forms.TextInput(attrs={'class' : 'input'}))
    phone = forms.CharField(label='Notification Phone Number', max_length=20, required=False, widget=forms.TextInput(attrs={'class' : 'input'}))

    class Meta:
        model = Vehicle
        fields = ('year','make','model','trim','mileage','email','phone', )

class NewMaintenance(forms.ModelForm):


    class Meta:
        model = Maintenance
        fields = (,)