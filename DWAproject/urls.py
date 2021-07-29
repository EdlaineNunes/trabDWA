from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('painelcontrole/', admin.site.urls),
    path('', include('DWAapp.urls')),
]
