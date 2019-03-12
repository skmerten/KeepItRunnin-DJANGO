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
from app.forms import NewVehicle, NewPart, PartHistory, NewUserForm, BootstrapAuthenticationForm

# Needs Updates
@login_required(login_url='/login')
def partHome(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/partsHome.html',
        {
            'title':'Parts',
            'year':datetime.now().year,
            'parts': Part.objects.filter(maintenance__vehicle__user = request.user),
            'partOptions' : True
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
            maintenance = Maintenance_Record.objects.all()
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/home.html',
                {
                    'title':'KeepItRunnin''',
                    'year':datetime.now().year,
                    'parts':parts,
                    'maint':maintenance,
                    'partOptions' : True
                }
            )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addPart.html',
        {
            'title':'Add Part',
            'year':datetime.now().year,
            'newPart': NewPart(user = request.user),
            'partOptions' : True
        }
    )

# Needs Updates
@login_required(login_url='/login')
def viewPart(request):
    part = Part.objects.filter(status=0)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewPart.html',
        {
            'title':'View All Parts',
            'year':datetime.now().year,
            'parts': part,
            'partOptions' : True
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
            'title':'Part Purchase History''',
            'year':datetime.now().year,
            'maintenanceHistory': Maintenance_Record.objects.all(),
            'partOptions' : True
        }
    )

# Needs Updates
@login_required(login_url='/login')
def logPart(request):
    if request.method == 'POST':
        form = PartHistory(request.user, request.POST)
        if form.is_valid():
            form.save()
            part = Part.objects.get(id = request.POST['part'])
            part.status = True
            part.save()
                      
            part_hist = Part_History.objects.filter(part__maintenance__vehicle__user = request.user)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/viewPartHist.html',
                {
                    'title':'Part Purchase History',
                    'year':datetime.now().year,
                    'part':part_hist,
                    'partOptions' : True
                }
            )

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/logPart.html',
        {
            'title':'Purchased Part',
            'year':datetime.now().year,
            'form': PartHistory(user = request.user),
            'partOptions' : True
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
            'title':'Select Part',
            'year':datetime.now().year,
            'selectMaint': form,
            'partOptions' : True
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
            'title':'Edit Part',
            'year':datetime.now().year,
            'newMaintenance': form,
            'partOptions' : True
        }
    )

@login_required(login_url='/login')
def viewPartHist(request):
    part_hist = Part_History.objects.filter(part__maintenance__vehicle__user = request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/viewPartHist.html',
        {
            'title':'Part Purchase History',
            'year':datetime.now().year,
            'part':part_hist,
            'partOptions' : True
        }
    )