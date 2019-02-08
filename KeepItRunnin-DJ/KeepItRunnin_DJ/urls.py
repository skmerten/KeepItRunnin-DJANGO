"""
Definition of urls for KeepItRunnin_DJ.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include
admin.autodiscover()

urlpatterns = [
    
    # /home 
    path('', app.views.newHome, name='newHome'),
    path('home/', app.views.home, name='home'),

    
    # /maintenance URLs
    path('maintenance/', app.views.maintenanceHome, name='maintenanceHome'),
    path('maintenance/history/', app.views.viewMaintHist, name='viewMaintHist'),
    path('maintenance/log/', app.views.logMaint, name='logMaint'),
    path('maintenance/add/', app.views.addMaint, name='addMaint'),
    path('maintenance/view/', app.views.viewMaint, name='viewMaint'),
    path('maintenance/select/', app.views.chooseMaint, name='chooseMaint'),
    path('maintenance/select/edit', app.views.editMaint, name='editMaint'),

    # /parts URLs
    path('parts/', app.views.partHome, name='partHome'),
    path('parts/history/', app.views.viewPartHist, name='viewPartHist'),
    path('parts/log/', app.views.logPart, name='logPart'),
    path('parts/add/', app.views.addPart, name='addPart'),
    path('parts/view/', app.views.viewPart, name='viewPart'),
    path('parts/select/', app.views.choosePart, name='choosePart'),
    path('parts/select/edit', app.views.editPart, name='editPart'),

    # /vehicleProfile URLs
    path('vehicle/', app.views.vehicleHome, name='vehicleHome'),
    path('vehicle/add/', app.views.addVehicle, name='addVehicle'),
    path('vehicle/checkIn/', app.views.checkIn, name='checkIn'),

    # Users
    path('newUser/', app.views.addUser, name='addUser'),


    # Login / Logout URLS
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     path('admin/', admin.site.urls),
]
