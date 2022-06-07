from django.db import models

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

    
