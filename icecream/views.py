from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate,login
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html")

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"home.html")

def loginuser(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        if request.method == "POST":
            uname = request.POST.get('username')
            upassword = request.POST.get('password')
            user = authenticate(username=uname, password=upassword)
            if user is not None:
                login(request,user)
                return redirect("/home")
            else:
                return render(request,"login.html")
        return render(request,"login.html")


def logoutuser(request):
    logout(request)
    return redirect("/login")

def registeruser(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, template_name="register.html", context={"register_form":form})
    