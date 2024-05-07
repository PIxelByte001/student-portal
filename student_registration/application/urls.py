from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.application_view, name='view_application'),
    path('form/', views.application_form, name='application_form'),
    path('form/submit', views.submit, name='application_submit')

]