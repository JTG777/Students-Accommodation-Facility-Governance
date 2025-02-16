from django.contrib import admin
from .models import Room,RoomAssign,Hostel,Warden,FeesMethod,RoomFeeStructure,Payment

# Register your models here.

class Roomadmin(admin.ModelAdmin):
    list_display=['room_no','room_type','hostel','room_max_capacity','room_alloted']

class Hosteladmin(admin.ModelAdmin):
    list_display=['hostel_type','warden']


class RoomAssignadmin(admin.ModelAdmin):
    list_display="__all__"


admin.site.register(Room,Roomadmin)
admin.site.register(Hostel,Hosteladmin)
admin.site.register(RoomAssign)
admin.site.register(FeesMethod)
admin.site.register(Warden)
admin.site.register(RoomFeeStructure)
admin.site.register(Payment)    