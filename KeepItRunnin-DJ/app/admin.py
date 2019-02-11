from django.contrib import admin
from .models import Vehicle, Maintenance, Maintenance_History, Part, Part_History

admin.site.register(Vehicle)
admin.site.register(Maintenance)
admin.site.register(Maintenance_History)
admin.site.register(Part)
admin.site.register(Part_History)