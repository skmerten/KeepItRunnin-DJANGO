"""
Definition of urls for KeepItRunnin_DJ.
"""

from datetime import datetime
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
    url(r'^$', app.views.home, name='home'),

    url(r'^addMaint/', app.views.addMaint, name='addMaint'),
    url(r'^addParts/', app.views.addParts, name='addParts'),
    url(r'^addVehicle/', app.views.addVehicle, name='addVehicle'),
    url(r'^checkIn/', app.views.checkIn, name='checkIn'),
    url(r'^editMaint/', app.views.editMaint, name='editMaint'),
    url(r'^histMaint/', app.views.histMaint, name='histMaint'),
    url(r'^logMaint/', app.views.logMaint, name='logMaint'),
    url(r'^maintenance/', app.views.maintenanceHome, name='maintenanceHome'),
    url(r'^parts/', app.views.partsHome, name='partsHome'),
    url(r'^vehicleProfile/', app.views.vehicleProfile, name='vehicleProfile'),
    url(r'^viewMaint/', app.views.viewMaint, name='partsHome'),
    url(r'^viewParts/', app.views.viewPart, name='viewPart'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),
]
