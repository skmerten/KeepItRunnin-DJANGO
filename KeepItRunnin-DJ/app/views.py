"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404
from django.template import RequestContext
from datetime import datetime
from app.models import Vehicle, Maintenance, Maintenance_History, Part

def home(request):
    parts = Part.objects.all()
    maintenance = Maintenance_History.objects.filter(next_due_date__lte=datetime.now())
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'parts':parts,
            'maint':maintenance
        }
    )

def vehicleProfile(request):
    """Renders the home page."""
    vehicle = Vehicle.objects.get(active=1)
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

def maintenanceHome(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/maintenanceHome.html',
        {
            'title':'Maintenance',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

def changeVehicle(request):
    allVehicle = Vehicle.objects.all()
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/changeVehicle.html',
        {
            'title':'Choose Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle,
            'allVehicle':allVehicle
        }
    )

def partsHome(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/partsHome.html',
        {
            'title':'Parts',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

def checkIn(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/checkIn.html',
        {
            'title':'Check In',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

# NEED UPDATE
def addVehicle(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/checkIn.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

# NEED UPDATE
def addMaint(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def viewMaint(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def histMaint(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def logMaint(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def logMaint(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def viewVehicle(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def editMaint(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def editMaint(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

# NEED UPDATE
def vehicleUpdate(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def requestPart(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def viewPart(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def showParts(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def vehicleUpdate(request):
    vehicle = Vehicle.objects.get(active=1)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )
