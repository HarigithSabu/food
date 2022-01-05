from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth
from accounts.models import register

# Create your views here.


def register(request):
    if request.method=="POST":
        first_name =request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.info(request,"username taken")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('register')
        else:
            register=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            register.save();
            print("user created")
            return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info(request,"invalid details")
            return redirect('login')
    else :
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')