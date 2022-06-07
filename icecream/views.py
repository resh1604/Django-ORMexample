from multiprocessing import context
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from icecream.models import Userdata

# Create your views here

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


#import userdata from models with all its objects and save into display
#render into html page and send display along.....data will be the array used to fetch in html page
def showuserlist(request):
    display = Userdata.objects.all()
    return render(request, "userslist.html", {"data": display})

def showuserprofile(request):
    user = request.user.id
    return render(request, "userprofile.html",{'use':user})

#FIRST- we will check if there is any POST data coming or not
#SECOND - we will put all post data into the variable form
#THIRD - we will check if the incoming data is valid or not
#FOURTH - before saving, it will refer the form for "model" variable, it now checks that the model is "Userdata"
#FIFTH - the form will be saved and redirected
def registeruser(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else:
        form = RegisterForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                # uname = form.cleaned_data.get('username')
                # upassword = form.cleaned_data.get('password')
                # user = authenticate(request,username=uname, password=upassword)
                # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request,"Registered Successfully")
                return redirect("/login")
        else:
            messages.error(request,form.errors)
            context = {'form': form}
            return render(request, "register.html", context)
