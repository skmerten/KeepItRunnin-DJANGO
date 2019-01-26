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
    path('', app.views.home, name='home'),
    
    # /maintenance URLs
    path('maintenance/', app.views.maintenanceHome, name='maintenanceHome'),
    #path('maintenance/edit/', app.views.editMaint, name='editMaint'),
    path('maintenance/history/', app.views.histMaint, name='histMaint'),
    path('maintenance/log/', app.views.logMaint, name='logMaint'),
    path('maintenance/add/', app.views.addMaint, name='addMaint'),
    path('maintenance/view/', app.views.viewMaint, name='viewMaint'),
    path('maintenance/select/', app.views.chooseMaint, name='chooseMaint'),
    path('maintenance/select/edit', app.views.editMaint, name='editMaint'),

    # /parts URLs
    path('parts/', app.views.partsHome, name='partsHome'),
    path('parts/add/', app.views.addParts, name='addParts'),
    path('parts/view/', app.views.viewPart, name='viewPart'),

    # /vehicleProfile URLs
    path('vehicle/', app.views.vehicleProfile, name='vehicleProfile'),
    path('vehicle/add/', app.views.addVehicle, name='addVehicle'),
    path('vehicle/checkIn/', app.views.checkIn, name='checkIn'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     path('admin/', admin.site.urls),
]
