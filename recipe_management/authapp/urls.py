from django.contrib import admin
from django.urls import path,include
from recipes import views
from authapp import views

urlpatterns = [

    path('register/',views.user_register),
    path('login/',views.user_login),
    path('logout/',views.user_logout),
]