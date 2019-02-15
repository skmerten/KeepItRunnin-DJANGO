from django.contrib import admin
from vehicles.models import Vehicle
from maintenance.models import Maintenance, Maintenance_History
from parts.models import Part, Part_History
from feed.models import Post

admin.site.register(Vehicle)
admin.site.register(Maintenance)
admin.site.register(Maintenance_History)
admin.site.register(Part)
admin.site.register(Part_History)
admin.site.register(Post)