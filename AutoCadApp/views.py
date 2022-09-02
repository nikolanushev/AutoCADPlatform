import datetime

from django.shortcuts import render
from .models import Tutorial, AppUser
from django.contrib.auth.models import User
# Create your views here.


def dashboard(request):
    tutorials = Tutorial.objects.all()[:3]
    user = AppUser.objects.filter(user=request.user).get()
    context = {"date": datetime.datetime.now(), "tutorials": tutorials, 'user': user}
    return render(request, 'dashboard.html', context=context)


def lectures(request):
    tutorials = Tutorial.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'tutorials': tutorials, 'user': user}
    return render(request, 'lectures.html', context)


def exams(request):
    user = AppUser.objects.filter(user=request.user).get()
    context = {'user': user}
    return render(request, 'exams.html', context=context)


def projects(request):
    user = AppUser.objects.filter(user=request.user).get()
    context = {'user': user}
    return render(request, 'projects.html', context=context)


def profile(request):
    user = AppUser.objects.filter(user=request.user).get()
    context = {'user': user}
    return render(request, 'profile.html', context=context)
