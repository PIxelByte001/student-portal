from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('signup/register', addstudent, name = 'register'),
    path('login/', signin, name = 'login'),
    path('login/next/', trylogin, name = 'identify'),
    path('logout/', logout_view, name = 'logout'),
    path('applications/', view_applications, name = 'application_view'),

]