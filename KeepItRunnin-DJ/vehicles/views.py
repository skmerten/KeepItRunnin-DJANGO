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
from app.forms import ChooseVehicle, DeleteVehicle, NewVehicle, NewMaintenance, ChooseMaintenance, NewMaintenanceHistory, NewPart, PartHistory, NewUserForm, BootstrapAuthenticationForm

@login_required(login_url='/login')
def addVehicle(request):
    if request.method == 'POST':
        form = NewVehicle(request.POST, request.FILES)
        
        if form.is_valid():
            id = request.POST['id']
            if id:
                vehicle = Vehicle.objects.get(pk = id)
                vehicle.year = request.POST['year']
                vehicle.make = request.POST['make']
                vehicle.model = request.POST['model']
                vehicle.trim = request.POST['trim']
                vehicle.mileage = request.POST['mileage']
                if len(request.FILES) != 0:
                    vehicle.image = request.FILES['image']
                vehicle.save()
            else:
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
                    'newVehicle':form
                }
            )
    else:
        user = User.objects.get(id=request.user.id)
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/addVehicle.html',
            {
                'title':'Add Vehicle',
                'year':datetime.now().year,
                'newVehicle':NewVehicle(initial={'user':user})
            }
        )

@login_required(login_url='/login')
def deleteVehicle(request):
    if request.method == 'POST':
        form = DeleteVehicle(request.user, request.POST)
        if form.is_valid():
            vehicle = Vehicle.objects.filter(pk = request.POST['vehicles'])
            vehicle.delete()

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
            'app/deleteVehicle.html',
            {
                'title':'Delete Vehicle',
                'year':datetime.now().year,
                'vehicles':DeleteVehicle(user = request.user)
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
def editVehicle(request):
    pk = request.POST['vehicle']
    vehicle = Vehicle.objects.get(id = pk)
    form = NewVehicle(initial={
            'id': pk,
            'year': vehicle.year,
            'make': vehicle.make,
            'model': vehicle.model,
            'trim': vehicle.trim,
            'mileage':vehicle.mileage,
            'image':vehicle.image,
        })

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addVehicle.html',
        {
            'title':'Edit Vehicle',
            'year':datetime.now().year,
            'newVehicle': form
        }
    )

# Needs Updates
@login_required(login_url='/login')
def chooseVehicle(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chooseVehicle.html',
        {
            'title':'Choose Vehicle',
            'year':datetime.now().year,
            'vehicle': ChooseVehicle(user = request.user)
        }
    )