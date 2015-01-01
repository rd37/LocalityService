from django.contrib import admin

# Register your models here.
from locality3d.models import location

class location_admin(admin.ModelAdmin):
    list_display=('id','lat','lng','height','name')
    list_filter=('id','lat','lng','height','name')
    
admin.site.register(location,location_admin)