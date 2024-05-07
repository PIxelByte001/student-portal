from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from student.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('student/', include('student.urls')),
    path('application/', include('application.urls')),
    path('administration/', include('administer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
