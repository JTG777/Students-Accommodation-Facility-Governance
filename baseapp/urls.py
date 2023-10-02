from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('studentdetails/',views.studentdetails,name='studdetails'),
    path('roomassign/',views.roomassign,name='roomassign'),
    path('managestudents/',views.displaystudent,name='display'),
    path('managestudents/update/<int:pk>/',views.updatestudent,name='update_student'),
    path('managestudents/delete/<int:pk>/',views.deletestudent,name='delete_student'),
    path('viewstudentpayment/',views.view_student_payment,name='stud_payment'),
]
