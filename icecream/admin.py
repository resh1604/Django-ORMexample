from django.contrib import admin
from .models import Userdata

# Register your models here.

#IF YOU HAVE A CUSTOMED DATABASE MODEL, YOU NEED TO REGISTER IT HERE 
admin.site.register(Userdata)