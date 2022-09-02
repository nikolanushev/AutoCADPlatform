import datetime

from django.shortcuts import render
from .models import Tutorial
# Create your views here.


def dashboard(request):
    context = {"date": datetime.datetime.now()}
    return render(request, 'dashboard.html', context=context)


def lectures(request):
    return render(request, 'lectures.html')


def exams(request):
    return render(request, 'exams.html')


def projects(request):
    return render(request, 'projects.html')

def profile(request):
    return render(request, 'profile.html')