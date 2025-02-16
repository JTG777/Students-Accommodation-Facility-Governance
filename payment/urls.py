from django.urls import path
from . import views

app_name='payment'

urlpatterns = [
    path('create-order/<int:payment_id>/<str:payment_type>/', views.create_razorpay_order, name='create_razorpay_order'),
    path('verify-payment/',views.verify_payment,name='verify_payment'),
    
]
