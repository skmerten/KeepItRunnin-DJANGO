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

    path('maintenance/addMaint/', app.views.addMaint, name='addMaint'),
    path('maintenance/addParts/', app.views.addParts, name='addParts'),
    path('vehicleProfile/addVehicle/', app.views.addVehicle, name='addVehicle'),
    path('vehicleProfile/checkIn/', app.views.checkIn, name='checkIn'),
    path('maintenance/editMaint/', app.views.editMaint, name='editMaint'),
    path('maintenance/histMaint/', app.views.histMaint, name='histMaint'),
    path('maintenance/logMaint/', app.views.logMaint, name='logMaint'),
    path('maintenance/', app.views.maintenanceHome, name='maintenanceHome'),
    path('parts/', app.views.partsHome, name='partsHome'),
    path('vehicleProfile/', app.views.vehicleProfile, name='vehicleProfile'),
    path('maintenance/viewMaint/', app.views.viewMaint, name='viewMaint'),
    path('maintenance/viewParts/', app.views.viewPart, name='viewPart'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     path('admin/', admin.site.urls),
]
