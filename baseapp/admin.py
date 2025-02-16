from django.contrib import admin
from django.http.request import HttpRequest

from .models import Student
# # from .models import Customuser
from .models import Course,OneteamBranch,Trainer




class OneteamBranchadmin(admin.ModelAdmin):
    list_display=['branch_name','isactive']

    def has_delete_permission(self, request: HttpRequest, obj=None):
        return False
    
class TrainerAdmin(admin.ModelAdmin):
    list_display=['trainer_name','course','branch']

# # Register your models here.
admin.site.register(Student)
# # admin.site.register(Customuser)
admin.site.register(Course)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(OneteamBranch, OneteamBranchadmin)
