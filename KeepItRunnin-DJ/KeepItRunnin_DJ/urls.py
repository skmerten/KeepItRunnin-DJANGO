"""
Definition of urls for KeepItRunnin_DJ.
"""

from datetime import datetime
from django.urls import path
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

    path('addMaint/', app.views.addMaint, name='addMaint'),
    path('addParts/', app.views.addParts, name='addParts'),
    path('addVehicle/', app.views.addVehicle, name='addVehicle'),
    path('checkIn/', app.views.checkIn, name='checkIn'),
    path('editMaint/', app.views.editMaint, name='editMaint'),
    path('histMaint/', app.views.histMaint, name='histMaint'),
    path('logMaint/', app.views.logMaint, name='logMaint'),
    path('maintenance/', app.views.maintenanceHome, name='maintenanceHome'),
    path('parts/', app.views.partsHome, name='partsHome'),
    path('vehicleProfile/', app.views.vehicleProfile, name='vehicleProfile'),
    path('viewMaint/', app.views.viewMaint, name='partsHome'),
    path('viewParts/', app.views.viewPart, name='viewPart'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     path('admin/', admin.site.urls),
]
