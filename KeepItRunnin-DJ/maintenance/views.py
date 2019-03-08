from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from vehicles.models import Vehicle
from parts.models import Part, Part_History
from maintenance.models import Maintenance, Maintenance_Record
from maintenance.forms import NewMaintenance, NewMaintenanceHistory, ChooseMaintenance
from maintenance.forms import NewOilChange

@login_required(login_url='/login')
def maintenanceHome(request):
    maintenance = Maintenance.objects.filter(vehicle__user = request.user)
    maint_hist = Maintenance_Record.objects.filter(maintenance__vehicle__user = request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/maintenanceHome.html',
        {
            'title':'Maintenance',
            'year':datetime.now().year,
            'maintenance':maintenance,
            'maint_hist':maint_hist,
            'maintOptions':True
        }
    )

@login_required(login_url='/login')
def addMaint(request):
    if request.method == 'POST':
        form = NewMaintenance(request.user, request.POST)
        # VERIFY NOT ALREADY EXIST
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
            else:
                form.save()
            maintenance = Maintenance.objects.get(name = request.POST['name'], description = request.POST['description'])
            # render Home Page
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/logMaint.html',
                {
                    'title':'Maintenance',
                    'year':datetime.now().year,
                    'form': NewMaintenanceHistory(user=request.user, initial={'maintenance':maintenance,'completed': 0}),
                    'postAdd':True,
                }
            )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addMaint.html',
        {
            'title':'Add Maintenance Plan',
            'year':datetime.now().year,
            'form': NewMaintenance(user = request.user),
        }
    )

@login_required(login_url='/login')
def chooseMaint(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chooseMaint.html',
        {
            'title':'Select Maintenance',
            'year':datetime.now().year,
            'selectMaint': ChooseMaintenance(user = request.user)
        }
    )

@login_required(login_url='/login')
def editMaint(request):
    pk = request.POST['maintenance']
    maintenance = Maintenance.objects.get(id = pk)
    form = NewMaintenance(user = request.user, initial={
            'id': pk,
            'vehicle':maintenance.vehicle,
            'name': maintenance.name,
            'description': maintenance.description,
            'months': maintenance.months, 
            'miles': maintenance.miles,
            'materials':maintenance.materials,
            'comments':maintenance.comments,

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
            # Most Recent Log Maint
            maintenance = Maintenance.objects.get(id = request.POST['maintenance'])
            if Maintenance_Record.objects.filter(maintenance__id = request.POST['maintenance']):
                record = Maintenance_Record.objects.get(maintenance__id = request.POST['maintenance'], completed = 0)
                record.completed = 1
                record.save()
            
            vehicle = Vehicle.objects.get(pk = maintenance.vehicle.id)
            vehicle.mileage = request.POST['current_mileage']
            vehicle.save()

            form.save()
           

                      
            parts = Part.objects.all()
            maintenance = Maintenance_Record.objects.filter(maintenance__vehicle__user=request.user)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/viewMaintHist.html',
                {
                    'title':'Maintenance History',
                    'year':datetime.now().year,
                    'maintenanceHistory':maintenance
                }
            )

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/logMaint.html',
        {
            'title':'Log Maintenance',
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
            'title':'Maintenance',
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
            'title':'Maintenance History',
            'year':datetime.now().year,
            'maintenanceHistory': Maintenance_Record.objects.filter(maintenance__vehicle__user=request.user)
        }
    )