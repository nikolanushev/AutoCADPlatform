import datetime

from django.shortcuts import render
from .models import Tutorial, AppUser
# Create your views here.


def dashboard(request):
    tutorials = Tutorial.objects.all()[:3]
    context = {"date": datetime.datetime.now(), "tutorials": tutorials}
    return render(request, 'dashboard.html', context=context)


def lectures(request):
    tutorials = Tutorial.objects.all()
    #user = AppUser.objects.filter(username=request.user.username).all()
    context = {'tutorials': tutorials}
    return render(request, 'lectures.html', context)


def exams(request):
    return render(request, 'exams.html')


def projects(request):
    return render(request, 'projects.html')


def profile(request):
    return render(request, 'profile.html')