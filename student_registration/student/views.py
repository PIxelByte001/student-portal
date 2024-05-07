from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import stu_details
from application.models import applicationss
from django.contrib.auth import login, authenticate, logout


def home(request):
    if request.user.is_authenticated:
        context = {'ICard' : stu_details.objects.get(email=request.user)}
        return render(request, 'index/home.html', context)
    else:
        return redirect('login')

def addstudent(request):
    if request.method == 'POST':
        email = request.POST.get('username')

        student = User(
            username = email,
        )
        student.set_password(request.POST.get('password1'))
        student.save()

        studata = stu_details(
            email = User.objects.get(username=email),
            name = request.POST.get('Name'),
            contact = request.POST.get('Contact'),
        )
        studata.save()
    return redirect('home')


def signup(request):
    return render(request, 'registration/signup.html')

def signin(request):
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def trylogin(request):
    message = ''
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('email'),
            password = request.POST.get('password'),
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'Login failed!'
    return redirect('login')

def view_applications(request):
    try:
        context = {'applications' : applicationss.objects.get(email=str(request.user)), 'ICard' : stu_details.objects.get(email=request.user)}
    except:
        context = {'applications' : None, 'ICard' : stu_details.objects.get(email=request.user)}
    return render(request, 'index/applications.html', context)

    
