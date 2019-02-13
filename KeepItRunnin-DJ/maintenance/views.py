from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Vehicle, Maintenance, Maintenance_History, Part, Part_History
from app.forms import NewVehicle, NewMaintenance, ChooseMaintenance, NewMaintenanceHistory, NewPart, PartHistory, NewUserForm, BootstrapAuthenticationForm

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

