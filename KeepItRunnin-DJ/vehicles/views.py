from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from maintenance.models import Maintenance, Maintenance_Record
from parts.models import Part, Part_History
from maintenance.forms import NewMaintenance, NewMaintenanceHistory, ChooseMaintenance
from app.forms import ChooseVehicle, DeleteVehicle, NewVehicle, NewPart, PartHistory, NewUserForm, BootstrapAuthenticationForm

@login_required(login_url='/login')
def addVehicle(request):
    if request.method == 'POST':
        form = NewVehicle(request.POST, request.FILES)
        
        if form.is_valid():
            id = request.POST['id']
            if id:
                vehicle = Vehicle.objects.get(pk = id)
                vehicle.name = request.POST['name']
                vehicle.year = request.POST['year']
                vehicle.make = request.POST['make']
                vehicle.model = request.POST['model']
                vehicle.trim = request.POST['trim']
                vehicle.mileage = request.POST['mileage']
                vehicle.color = request.POST['color']
                vehicle.transmission = request.POST['transmission']
                vehicle.tankSize = request.POST['tankSize']
                vehicle.driveWheels = request.POST['driveWheels']
                vehicle.mpg = request.POST['mpg']
                vehicle.status = request.POST['status']

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
                    'vehicles': vehicles,
                    'vehicleOptions' : True
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
                    'form':form,
                    'vehicleOptions' : True
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
                'form':NewVehicle(initial={'user':user}),
                'vehicleOptions' : True
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
                    'vehicles': vehicles,
                    'vehicleOptions' : True
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
                'vehicles':DeleteVehicle(user = request.user),
                'vehicleOptions' : True
            }
        )



@login_required(login_url='/login')
def vehicleHome(request):
    vehicles = Vehicle.objects.filter(user = request.user)
    maintenance = Maintenance_Record.objects.filter(maintenance__vehicle__user = request.user, completed = 0)

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vehicleHome.html',
        {
            'title':'Vehicle',
            'year':datetime.now().year,
            'vehicles': vehicles,
            'maintenance': maintenance,
            'vehicleOptions' : True,
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
def editVehicle(request):
    pk = request.POST['vehicle']
    vehicle = Vehicle.objects.get(id = pk)
    form = NewVehicle(initial={
            'id': pk,
            'name': vehicle.name,
            'year': vehicle.year,
            'make': vehicle.make,
            'model': vehicle.model,
            'trim': vehicle.trim,
            'mileage':vehicle.mileage,
            'image':vehicle.image,
            'color': vehicle.color,
            'tankSize': vehicle.tankSize, 
            'transmission': vehicle.transmission,
            'driveWheels': vehicle.driveWheels,
            'mpg': vehicle.mpg,
            'status': vehicle.status
        })

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addVehicle.html',
        {
            'title':'Edit Vehicle',
            'year':datetime.now().year,
            'form': form,
            'vehicleOptions' : True
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
            'title':'Select Vehicle',
            'year':datetime.now().year,
            'vehicle': ChooseVehicle(user = request.user),
            'vehicleOptions' : True
        }
    )

@login_required(login_url='/login')
def vehicleProfile(request, id):
    if Vehicle.objects.filter(user = request.user, id = id).exists():
        vehicle = Vehicle.objects.get(user = request.user, id = id)
    else:
        vehicles = Vehicle.objects.filter(user = request.user)
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/vehicleHome.html',
            {
                'title':'Vehicle',
                'year':datetime.now().year,
                'vehicles': vehicles,
                'vehicleOptions' : True,
            }
        )
    maintenances = Maintenance.objects.filter(vehicle = vehicle)
    maintHist = Maintenance_Record.objects.filter(maintenance__vehicle = vehicle, completed = False)
    vehicleData = str(vehicle.year) + " " + vehicle.make + " " + vehicle.model + " " + vehicle.trim
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vehicleProfile.html',
        {
            'title':vehicleData,
            'year':datetime.now().year,
            'vehicle': vehicle,
            'maintenances': maintenances,
            'maintHist':maintHist,
            'vehicleOptions' : True,
        }
    )