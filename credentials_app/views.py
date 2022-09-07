from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']

        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

def register(request):
    if request.method == 'POST':
        phone = request.POST['phone']

        # profile=User.objects.create_user(username=username,phone=phone)

        user.save();
        # profile.save();

        print("user created");
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def temp(request):
    return render(request,'temp.html')