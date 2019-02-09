"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Vehicle, Maintenance, Maintenance_History, Part, Part_History
from app.forms import NewVehicle, NewMaintenance, ChooseMaintenance, NewMaintenanceHistory, NewPart, PartHistory, NewUserForm, BootstrapAuthenticationForm

def newHome(request):
    if request.user.is_authenticated:
        parts = Part.objects.filter(status = 0)
        maintenance = Maintenance_History.objects.filter(maintenance__vehicle__user=request.user)
        vehicles = Vehicle.objects.filter(user = request.user)
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/home.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
                'parts':parts,
                'maintenance':maintenance,
                'vehicles':vehicles
            }
        )
    else:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/overview_home.html',
            {
                'title':'Home Page',
                'year':datetime.now().year
            }
        )
# Needs Updates
def addUser(request):
    if request.method == 'POST':
        Users = User.objects.all()
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()

            # render Home Page
            parts = Part.objects.all()
            maintenance = Maintenance_History.objects.all()
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
    else:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/newUser.html',
            {
                'title':'New User',
                'year':datetime.now().year,
                'user':User()
            }
        )

@login_required(login_url='/login')
def home(request):
    parts = Part.objects.filter(status = 0)
    maintenance = Maintenance_History.objects.filter(completed=0, maintenance__vehicle__user=request.user)
    vehicles = Vehicle.objects.filter(user = request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'parts':parts,
            'maintenance':maintenance,
            'vehicles':vehicles
        }
    )

@login_required(login_url='/login')
def addVehicle(request):
    if request.method == 'POST':
        form = NewVehicle(request.POST)
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

@login_required(login_url='/login')
def addMaint(request):
    if request.method == 'POST':
        form = NewMaintenance(request.user, request.POST)
        if form.is_valid():
            id = request.POST['id']
            if id:
                record = Maintenance.objects.get(pk = id)
                record.vehicle = Vehicle.objects.get(id = request.POST['vehicle'])
                record.name = request.POST['name']
                record.description = request.POST['description']
                record.months = request.POST['months']
                record.miles = request.POST['miles']
                record.materials = request.POST['materials']
                record.comments = request.POST['comments']
                record.save()

                parts = request.POST['materials'].split(",")
                #part = Part()
                print(parts)
                
            else:
                form.save()

            # render Home Page
            maintenance = Maintenance.objects.filter(vehicle__user=request.user)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/viewMaint.html',
                {
                    'title':'Maintenance',
                    'year':datetime.now().year,
                    'maintenance': maintenance
                }
            )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addMaint.html',
        {
            'title':'Add Maintenance',
            'year':datetime.now().year,
            'newMaintenance': NewMaintenance(user = request.user)
        }
    )

# Needs Updates
@login_required(login_url='/login')
def chooseMaint(request):
    maintenance = Maintenance.objects.all()
    form = ChooseMaintenance()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chooseMaint.html',
        {
            'title':'Choose Maintenance',
            'year':datetime.now().year,
            'selectMaint': form
        }
    )

# Needs Updates
@login_required(login_url='/login')
def editMaint(request):
    pk = request.POST['maintenance']
    maintenance = Maintenance.objects.get(id = pk)
    form = NewMaintenance(initial={
            'id': pk,
            'vehicle':maintenance.vehicle,
            'name': maintenance.name,
            'description': maintenance.description,
            'months': maintenance.months, 
            'miles': maintenance.miles,
            'materials':maintenance.materials,
            'comments':maintenance.comments
        })
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addMaint.html',
        {
            'title':'Edit Maintenance',
            'year':datetime.now().year,
            'newMaintenance': form
        }
    )

# Needs Updates
@login_required(login_url='/login')
def logMaint(request):
    if request.method == 'POST':
        form = NewMaintenanceHistory(request.user, request.POST)
        if form.is_valid():
            form.save()
            maintenance = Maintenance.objects.get(id = request.POST['maintenance'])
            vehicle = Vehicle.objects.get(pk = maintenance.vehicle.id)
            vehicle.mileage = request.POST['current_mileage']
            vehicle.save()
                      
            parts = Part.objects.all()
            maintenance = Maintenance_History.objects.filter(maintenace__vehicle__user=request.user)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/viewMaintHist.html',
                {
                    'title':'Maintenance History',
                    'year':datetime.now().year,
                    'maint':maintenance
                }
            )

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/logMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'form':NewMaintenanceHistory(user=request.user, initial={'completed': 0})
        }
    )

@login_required(login_url='/login')
def viewMaint(request):
    maintenance = Maintenance.objects.filter(vehicle__user=request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaint.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'maintenance': maintenance
        }
    )

# Needs Updates
@login_required(login_url='/login')
def viewMaintHist(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaintHist.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'maintenanceHistory': Maintenance_History.objects.filter(maintenance__vehicle__user=request.user)
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
def maintenanceHome(request):
    maintenance = Maintenance.objects.filter(vehicle__user = request.user)
    maint_hist = Maintenance_History.objects.filter(maintenance__vehicle__user = request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/maintenanceHome.html',
        {
            'title':'Maintenance',
            'year':datetime.now().year,
            'maintenance':maintenance,
            'maint_hist':maint_hist,
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
def partHome(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/partsHome.html',
        {
            'title':'Parts',
            'year':datetime.now().year
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

# Needs Updates
@login_required(login_url='/login')
def addPart(request):
    if request.method == 'POST':
        form = NewPart(request.user, request.POST)
        if form.is_valid():
            id = request.POST['id']
            if id:
                record = Part.objects.get(pk = id)
                record.maintenance = Maintenance.objects.get(id = request.POST['maintenance'])
                record.part_name = request.POST['part_name']
                record.part_description = request.POST['part_description']
                record.date_requested = request.POST['date_requested']
                record.need_by_date = request.POST['need_by_date']
                record.comments = request.POST['comments']
                record.status = request.POST['status']
                record.save()
            else:
                form.save()

            # render Home Page
            parts = Part.objects.all()
            maintenance = Maintenance_History.objects.all()
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
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addPart.html',
        {
            'title':'Add Part',
            'year':datetime.now().year,
            'newPart': NewPart(user = request.user)
        }
    )

# Needs Updates
@login_required(login_url='/login')
def viewPart(request):
    part = Part.objects.filter(completed=0)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewPart.html',
        {
            'title':'View All Parts',
            'year':datetime.now().year,
            'parts': part
        }
    )

# Needs Updates
@login_required(login_url='/login')
def viewPartHist(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewMaintHist.html',
        {
            'title':'Add Vehicle',
            'year':datetime.now().year,
            'maintenanceHistory': Maintenance_History.objects.all()
        }
    )

# Needs Updates
@login_required(login_url='/login')
def logPart(request):
    if request.method == 'POST':
        form = PartHistory(request.POST)
        if form.is_valid():
            id = request.POST['id']
            if id:
                record = Part.objects.get(pk = id)
                record.maintenance = Maintenance.objects.get(id = request.POST['maintenance'])
                record.part_name = request.POST['part_name']
                record.part_description = request.POST['part_description']
                record.date_requested = request.POST['date_requested']
                record.need_by_date = request.POST['need_by_date']
                record.comments = request.POST['comments']
                record.status = request.POST['status']
                record.save()
            else:
                part = Part.objects.get(pk = request.POST['part'])
                part.status = "True"
                part.save()
                form.save()
                      
            parts = Part.objects.all()
            maintenance = Maintenance_History.objects.filter(next_due_date__lte=datetime.now())
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/viewPartHist.html',
                {
                    'title':'Part History',
                    'year':datetime.now().year,
                    'part':Part_History.objects.all()
                }
            )

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/logMaint.html',
        {
            'title':'Log Part',
            'year':datetime.now().year,
            'form': PartHistory()
        }
    )

# Needs Updates
@login_required(login_url='/login')
def choosePart(request):
    maintenance = Maintenance.objects.all()
    form = ChooseMaintenance()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chooseMaint.html',
        {
            'title':'Choose Maintenance',
            'year':datetime.now().year,
            'selectMaint': form
        }
    )

# Needs Updates
@login_required(login_url='/login')
def editPart(request):
    pk = request.POST['maintenance']
    maintenance = Maintenance.objects.get(id = pk)
    form = NewMaintenance(initial={
            'id': pk,
            'name': maintenance.name,
            'description': maintenance.description,
            'months': maintenance.months, 
            'miles': maintenance.miles,
            'materials':maintenance.materials,
            'comments':maintenance.comments
        })
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addMaint.html',
        {
            'title':'Edit Maintenance',
            'year':datetime.now().year,
            'newMaintenance': form
        }
    )