"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import json, html 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'title': 'Vehicle Information',
            'vehicleYear': 'test',
            'make':'test',
            'model':'test',
            'trim':'test',
            'mileage':'test',
            'maint':'test',
            'driveable':'test',
            'checkin':'test',
        }
    )
