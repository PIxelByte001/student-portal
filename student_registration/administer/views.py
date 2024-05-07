from django.shortcuts import render, redirect, get_object_or_404
from student.models import stu_details
from application.models import applicationss
# Create your views here.


def manage(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context = {'students' : stu_details.objects.all()}
            return render(request, 'adminpanel.html', context)
        else:
            return redirect('home')
    else:
        return redirect('home')


def view_application(request, email):
    application = get_object_or_404(applicationss, email=email)
    return render(request, 'view_application.html', {'application': application})


def accept_application(request, email):
    student = get_object_or_404(stu_details, email=email)
    student.status=1
    student.save()
    return redirect('admin-panel')


def reject_application(request, email):
    student = get_object_or_404(stu_details, email=email)
    student.status=-1
    student.save()
    return redirect('admin-panel')
