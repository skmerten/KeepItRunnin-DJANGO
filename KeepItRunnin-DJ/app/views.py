"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import json, html 
from app.models import Vehicle, Maintenance, Maintenance_History, Part

def home(request):
    vehicle = Vehicle.objects.get(active=1)
    print(vehicle)
    print(vehicle.year)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

def vehicleProfile(request):
    """Renders the home page."""
    vehicle = Vehicle.objects.all(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vehicleProfile.html',
        {
            'title':'Choose Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )
