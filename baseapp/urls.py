from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('student-register/',views.student_register,name='student_register'),
    path('managestudents/',views.displaystudent,name='display'),
    path('managestudents/update/<int:pk>/',views.updatestudent,name='update_student'),
    path('managestudents/delete/<int:pk>/',views.deletestudent,name='delete_student'),
    path('get-trainers/', views.get_trainers, name='get_trainers'),
    
    
]
