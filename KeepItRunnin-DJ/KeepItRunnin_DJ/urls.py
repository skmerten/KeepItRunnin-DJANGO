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

    # /vehicleProfile

    url(r'^vehicleProfile/', app.views.vehicleProfile, name='vehicleProfile'),
    url(r'^changeVehicle/', app.views.changeVehicle, name='changeVehicle'),
    url(r'^maintenance/', app.views.maintenanceHome, name='maintenanceHome'),
    url(r'^parts/', app.views.partsHome, name='partsHome'),
    url(r'^checkIn/', app.views.checkIn, name='checkIn'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),
]
