from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:id>', produto, name='produto'),
]