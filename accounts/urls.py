from django.urls import path,include
from . import views

urlpatterns = [
    path('',include("django.contrib.auth.urls")),
    path('payment-dues/',views.payment_dues,name='payment_dues')
    
]
    





