from django.db import models

# Create your models here.
class userlist(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

