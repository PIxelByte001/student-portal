from django.urls import path
from .views import *


urlpatterns = [
    path('adminpanel/', manage, name = 'admin-panel'),
    path('view-application/<str:email>/', view_application, name='view_application'),
    path('accept-application/<str:email>/', accept_application, name='accept_application'),
    path('reject-application/<str:email>/', reject_application, name='reject_application'),
]