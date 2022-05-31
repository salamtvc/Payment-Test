from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    # url to retrive auth token.
    path('token/', views.obtain_auth_token)
]