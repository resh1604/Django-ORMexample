from dataclasses import fields
from django import forms
from .models import Userdata


# Create your forms here.
class RegisterForm(forms.ModelForm):
	class Meta:
		model = Userdata   #DEFINE MODEL NAME
		fields = ['username','email','firstname','lastname','age','password']  #DEFINE COLUMN NAMES