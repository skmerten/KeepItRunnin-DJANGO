from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404
from django.template import RequestContext
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from vehicles.models import Vehicle
from maintenance.models import Maintenance, Maintenance_Record
from maintenance.forms import NewMaintenance, NewMaintenanceHistory, ChooseMaintenance
from parts.models import Part, Part_History
from app.forms import NewVehicle, NewPart, PartHistory, NewUserForm, BootstrapAuthenticationForm

def newHome(request):
    if request.user.is_authenticated:
        parts = Part.objects.filter(status = 0)
        maintenance = Maintenance_Record.objects.filter(completed=0, maintenance__vehicle__user=request.user)
        vehicles = Vehicle.objects.filter(user = request.user, 
                                          vehicle_creation__year = datetime.now().year,
                                          vehicle_creation__month = datetime.now().month,
                                          vehicle_creation__day = datetime.now().day)
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/home.html',
            {
                'title':'KeepItRunnin''',
                'year':datetime.now().year,
            }
        )
    else:
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/overview_home.html',
            {
                'title':'KeepItRunnin''',
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
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'app/home.html',
                {
                    'title':'Home Page',
                    'year':datetime.now().year,
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
    maintenance = Maintenance_Record.objects.filter(completed=0, maintenance__vehicle__user=request.user)
    vehicles = Vehicle.objects.filter(user = request.user, 
                                      vehicle_creation__year = datetime.now().year,
                                      vehicle_creation__month = datetime.now().month,
                                      vehicle_creation__day = datetime.now().day)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title':'KeepItRunnin''',
            'year':datetime.now().year,
        }
    )

def features(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/features.html',
        {
            'title':'KeepItRunnin''',
            'year':datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'KeepItRunnin''',
            'year':datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'KeepItRunnin''',
            'year':datetime.now().year,
        }
    )