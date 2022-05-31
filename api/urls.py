from rest_framework import routers
from django.urls import path
from api import views

urlpatterns = [ 
    path('payment/', views.UpdatePaymentView.as_view(), name='payment'),

    # API endpoint that generates an irregular response.
    path('check_payment_status/', views.CheckPaymentSatusView.as_view(), name="payment_status"),
]