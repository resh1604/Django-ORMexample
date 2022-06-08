from distutils.command.upload import upload
from email.policy import default
from operator import truediv
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import BaseUserManager, UserDataManager

# Create your models here.


#CUSTOM MODEL...WILL BE SHOWN SEPARATELY IN THE DATABASE
#DATABASE ADDS 'S' AFTER THE MODEL NAME
class Userdata(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()

    #THIS FUNCITON HELPS TO DISPLAY NAME OF THE OBJECT
    def __str__(self):
        return self.firstname + ' ' + self.lastname


#FUNCTION FOR UPLOADING IMAGE
def get_profile_image_filepath(self,filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "static/default.webp"


#ABSTRACT USER    
class TestUserData(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,null=True)
    date_joined = models.DateTimeField(verbose_name="datejoined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="lstlogin",auto_now=True)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,null=True,blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)
    #required fields
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserDataManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']

    def __str__(self):
        return self.username  #default return value if you dont access an individual field

    def has_perm(self,perm,obj=None):
        return self.is_admin    #default permission - override function - does the user have permission t do an adminish thing

    def has_module_perms(self,app_label):
        return True 

    def get_profile_image_filename(self): #when a user will save a profile image,at that time it will have some random name. this function will help to keep one common name for all user's profile image 
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]



