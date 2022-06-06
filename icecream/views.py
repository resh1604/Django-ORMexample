from multiprocessing import context
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from icecream.models import userlist

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")


def home(request):
    # DOUBT DOUBT DOUBT
    # AFTER THE REGSTRATION IT SENDS TO LOGIN FORM
    if request.user.is_anonymous:
       return redirect("/login")
    return render(request, "home.html")


def loginuser(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        if request.method == "POST":
            uname = request.POST.get('username')
            upassword = request.POST.get('password')
            user = authenticate(username=uname, password=upassword)
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                return render(request, "login.html")
        return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect("/login")


def registeruser(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        form = RegisterUserForm()

        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registered successfully")
                return redirect("/login")
            else:
                messages.error(request,form.errors)


        context = {'form': form}
        return render(request, "register.html", context)

def showuserlist(request):
    display = User.objects.all()
    return render(request, "userslist.html", {"userlist": display})

def showuserprofile(request):
    # display = User.objects.all()
    return render(request, "userprofile.html")
