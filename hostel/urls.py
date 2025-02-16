from django.urls import path
from . import views

urlpatterns = [
    
    path('roomassign/',views.roomassign,name='roomassign'),
    # path('viewstudentpayment/',viewspayment_d,name='payment_due'),
    path('manage-roomassign/',views.manage_roomassign,name='manage_roomassign'),
    path('delete-room-assign/<int:room_assign_id>',views.delete_room_assign,name='delete_room_assign'),


]