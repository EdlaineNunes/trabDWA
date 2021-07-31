from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('photogallery/', photogallery, name='photogallery'),
    path('courses/', courses, name='courses'),
    path('teachers/', teachers, name='teachers'),
    path('studentsall/', studentsall, name='studentsall'),
    path('student/<int:id>', student, name='student'),
]