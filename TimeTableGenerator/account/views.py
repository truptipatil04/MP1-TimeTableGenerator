from django.shortcuts import render
from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    # return render(request,'register.html')
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User taken')
                return redirect('register')  # register
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')  # register
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,
                first_name=first_name,last_name=last_name)
                print('usercreated')
                user.save()
                return redirect('login')        # login
        else:
            messages.info(request,'password not matching')
            return redirect('register')     # register
        # return redirect('acc')

    else:
        return render(request,'register.html') # register.html

def login(request):
    # return render(request,'login.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def info(request):
    return render(request,'info.html')
