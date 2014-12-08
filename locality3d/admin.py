from django.contrib import admin

# Register your models here.
from locality3d.models import location

class location_admin(admin.ModelAdmin):
    list_display=('id','lat','lng','height')
    list_filter=('id','lat','lng','height')
    
admin.site.register(location,location_admin)