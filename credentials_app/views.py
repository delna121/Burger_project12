from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account


# Create your views here.

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            request.session['email']=email
            request.session['name']=user.name
            # store user details in session
            request.session['district']=user.district
            return redirect('/')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('/')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        fname=request.POST['fname']
        # mun_name=request.POST['mun_name']
        lname=request.POST['lname']
        city=request.POST['city']
        state=request.POST['state']
        district=request.POST['district']
        # role=request.POST['role']
        phone_number=request.POST['tel']
        print(email,password,fname,lname,state,district,city,phone_number)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('/')
        # elif Account.objects.filter(fname=fname).exists():
        #     messages.error(request, 'username already exists')
        #     return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, fname=fname, lname=lname, state=state, district=district, city=city, phone_number=phone_number)
            user.save()
            messages.success(request, 'you are registered')
            return redirect('/')
    return render(request, 'register.html')

def index(request):
    return render(request,'index.html')

def temp(request):
    return render(request,'temp.html')