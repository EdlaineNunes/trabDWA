from django.shortcuts import render
from DWAapp.models import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def photogallery(request):
    return render(request, 'pages/photogallery.html')

def courses(request):
    return render(request, 'pages/courses.html')

def teachers(request):
    return render(request, 'pages/teachers.html')

def studentsall(request):
    studentsall = Students.objects.all()

    context = {
        'studentsall' : studentsall,
    }
    return render(request, 'pages/studentsall.html', context)

def student(request, id):
    student = Students.objects.get(id=id)
    context = {
        'student': student,
    }
    return render(request, 'pages/student.html', context)
