from django.contrib import admin
from django.http.request import HttpRequest

from .models import Student
# from .models import Customuser
from .models import Course
from .models import OneteamBranch
from .models import Trainer
from .models import Room
from .models import Hostel
from .models import RoomAssign
from .models import Fees


class Roomadmin(admin.ModelAdmin):
    list_display=['room_name','room_no','room_type','hostel',]

class Hosteladmin(admin.ModelAdmin):
    list_display=['hostel_type','caretaker']


class RoomAssignadmin(admin.ModelAdmin):
    list_display="__all__"

class OneteamBranchadmin(admin.ModelAdmin):
    list_display=['branch_name','isactive']

    def has_delete_permission(self, request: HttpRequest, obj=None):
        return False


# Register your models here.
admin.site.register(Student)
# admin.site.register(Customuser)
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(OneteamBranch, OneteamBranchadmin)
admin.site.register(Room,Roomadmin)
admin.site.register(Hostel,Hosteladmin)
admin.site.register(RoomAssign)
admin.site.register(Fees)