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
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vehicleProfile.html',
        {
            'title':'Choose Vehicle',
            'year':datetime.now().year,
        }
    )

def maintenanceHome(request):
    vehicle = Vehicle.objects.get()
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

# Below Will Be Removed
def changeVehicle(request):
    allVehicle = Vehicle.objects.all()
    vehicle = Vehicle.objects.get()
    if request.method == 'POST':
        form = ContactForm(request._load_post_and_files)
        if form.is_valid():
            print (form.cleaned_date['choice'])

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
    vehicle = Vehicle.objects.get()
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
    vehicle = Vehicle.objects.get()
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print (form.cleaned_date['year'])

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addVehicle.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
        }
    )

# NEED UPDATE
def addMaint(request):
    vehicle = Vehicle.objects.get()
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
    vehicle = Vehicle.objects.get()
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
    vehicle = Vehicle.objects.get()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/histMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def logMaint(request):
    vehicle = Vehicle.objects.get()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/logMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def viewVehicle(request):
    vehicle = Vehicle.objects.get()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewVehicle.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def editMaint(request):
    vehicle = Vehicle.objects.get()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/editMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

# NEED UPDATE
def vehicleUpdate(request):
    vehicle = Vehicle.objects.get()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/updateVehicle.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def addParts(request):
    vehicle = Vehicle.objects.get()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addParts.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )

#NEED UPDATE
def viewPart(request):
    vehicle = Vehicle.objects.get()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewPart.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'vehicle': vehicle
        }
    )
