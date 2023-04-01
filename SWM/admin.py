from django.contrib import admin
from  django.contrib.auth.models  import  Group

from SWM.models import static_route, realtime_location, collection_location

class Admin_static_route(admin.ModelAdmin):
    list_display = ('Time', 'Latitude', 'Longitude')

class Admin_realtime_route(admin.ModelAdmin):
    list_display = ('Date', 'Time', 'Latitude', 'Longitude', 'Weight')

class Admin_collection_center(admin.ModelAdmin):
    list_display = ('Start_date', 'Start_time', 'End_date', 'End_time', 'Latitude', 'Longitude', 'Phone', 'Garbage_type')


admin.site.register(static_route, Admin_static_route)
admin.site.register(realtime_location, Admin_realtime_route)
admin.site.register(collection_location, Admin_collection_center)

# Register your models here.
