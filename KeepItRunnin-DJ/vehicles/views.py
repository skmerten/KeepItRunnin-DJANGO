from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from maintenance.models import Maintenance, Maintenance_History
from parts.models import Part, Part_History
from app.forms import NewVehicle, NewMaintenance, ChooseMaintenance, NewMaintenanceHistory, NewPart, PartHistory, NewUserForm, BootstrapAuthenticationForm


@login_required(login_url='/login')
def addVehicle(request):
    if request.method == 'POST':
        form = NewVehicle(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()

            # render Home Page
            vehicles = Vehicle.objects.filter(user = request.user)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/vehicleHome.html',
                {
                    'title':'Vehicle',
                    'year':datetime.now().year,
                    'vehicles': vehicles
                }
            )
    else:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/addVehicle.html',
            {
                'title':'Add Vehicle',
                'year':datetime.now().year,
                'newVehicle':NewVehicle()
            }
        )


# Needs Updates
@login_required(login_url='/login')
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


@login_required(login_url='/login')
def vehicleHome(request):
    vehicles = Vehicle.objects.filter(user = request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vehicleHome.html',
        {
            'title':'Vehicle',
            'year':datetime.now().year,
            'vehicles': vehicles
        }
    )



# Needs Updates
@login_required(login_url='/login')
def checkIn(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/checkIn.html',
        {
            'title':'Check In',
            'year':datetime.now().year,
        }
    )

# Needs Updates
@login_required(login_url='/login')
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

# Needs Updates
@login_required(login_url='/login')
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
