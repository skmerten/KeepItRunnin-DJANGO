"""
Definition of urls for KeepItRunnin_DJ.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls.static import static
import app.forms
import app.views, maintenance.views, parts.views, vehicles.views
from KeepItRunnin_DJ import settings
# Uncomment the next lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include
admin.autodiscover()

urlpatterns = [
    
    # /home 
    path('', app.views.newHome, name='newHome'),
    path('home/', app.views.home, name='home'),
    path('about/', app.views.about, name='about'),
    path('features/', app.views.features, name='features'),
    path('contact/', app.views.contact, name='contact'),
    
    # /maintenance URLs
    path('maintenance/', maintenance.views.maintenanceHome, name='maintenanceHome'),
    path('maintenance/history/', maintenance.views.viewMaintHist, name='viewMaintHist'),
    path('maintenance/log/', maintenance.views.logMaint, name='logMaint'),
    path('maintenance/add/', maintenance.views.addMaint, name='addMaint'),
    path('maintenance/view/', maintenance.views.viewMaint, name='viewMaint'),
    path('maintenance/select/', maintenance.views.chooseMaint, name='chooseMaint'),
    path('maintenance/select/edit', maintenance.views.editMaint, name='editMaint'),

    # /parts URLs
    path('parts/', parts.views.partHome, name='partHome'),
    path('parts/history/', parts.views.viewPartHist, name='viewPartHist'),
    path('parts/log/', parts.views.logPart, name='logPart'),
    path('parts/add/', parts.views.addPart, name='addPart'),
    path('parts/view/', parts.views.viewPart, name='viewPart'),
    path('parts/select/', parts.views.choosePart, name='choosePart'),
    path('parts/select/edit', parts.views.editPart, name='editPart'),

    # /vehicleProfile URLs
    path('vehicle/', vehicles.views.vehicleHome, name='vehicleHome'),
    path('vehicle/add/', vehicles.views.addVehicle, name='addVehicle'),
    path('vehicle/checkIn/', vehicles.views.checkIn, name='checkIn'),
    path('vehicle/delete/', vehicles.views.deleteVehicle, name='deleteVehicle'),
    path('vehicle/select/', vehicles.views.chooseVehicle, name='chooseVehicle'),
    path('vehicle/select/edit', vehicles.views.editVehicle, name='editVehicle'),
    path('vehicle/profile/<int:id>', vehicles.views.vehicleProfile, name='vehicleProfile'),

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
