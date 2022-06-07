from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="icecream"),
    path('login',views.loginuser, name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('registeruser',views.registeruser,name="registeruser"),
    path('home',views.home,name="home"),
    path('showuserlist',views.showuserlist,name="showuserlist"),
    path('showuserprofile',views.showuserprofile,name="showuserprofile"),
]
