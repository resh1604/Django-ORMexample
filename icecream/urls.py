from django import views
from django.contrib import admin
from django.urls import path, include
from icecream import views

urlpatterns = [
    path('',views.index,name="icecream"),
    path('login',views.loginuser, name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('home',views.home,name="home"),
    path('register',views.registeruser,name="register"),
]