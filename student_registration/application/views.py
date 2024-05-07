from django.shortcuts import render, redirect
from django.contrib.auth import *
from .models import applicationss
from student.models import stu_details

def application_view(request):
    if request.user.is_authenticated:
        context = {'application' : applicationss.objects.get(email=str(request.user))}
        return render(request, 'applications.html', context)
    else:
        return redirect('login')
    
def application_form(request):
    return render(request, 'form.html')

def submit(request):
    if request.method=='POST':
        user = stu_details.objects.get(email=str(request.user))

        data = applicationss(
            email = user,
            Name = request.POST.get('name'),
            Mothers_Name = request.POST.get('Mname'),
            Fathers_Name = request.POST.get('Fname'),
            Address = request.POST.get('address'),
            Contact1 = request.POST.get('mobile1'),
            Contact2 = request.POST.get('mobile2'),
            Class_10 = request.POST.get('class10'),
            Class_12 = request.POST.get('class12'),
            UG_CGPA = request.POST.get('cgpa'),
            Course = request.POST.get('course'),
            Photograph = request.POST.get('photo'),
            Signature = request.POST.get('sign'),
        )
        data.save()

        confirm = stu_details(
            email = user,
            application_filled = True
        )
        confirm.save()
        return redirect('home')