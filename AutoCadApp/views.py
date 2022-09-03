import datetime

from django.shortcuts import render, redirect

from .forms import AddQuestionForm
from .models import Tutorial, AppUser, Hint, Project, Test, Link
from django.contrib.auth.models import User
# Create your views here.


def dashboard(request):
    usrs = AppUser.objects.all()[2:6]
    links = Link.objects.all()[:5]
    tutorials = Tutorial.objects.all()[:3]
    hints = Hint.objects.all()[2:5]
    user = AppUser.objects.filter(user=request.user).get()
    context = {"date": datetime.datetime.now(), "tutorials": tutorials, 'links': links, 'hints': hints, 'user': user, 'users': usrs}
    return render(request, 'dashboard.html', context=context)


def lectures(request):
    tutorials = Tutorial.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'tutorials': tutorials, 'user': user}
    return render(request, 'lectures.html', context)


def hints(request):
    hints = Hint.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'hints': hints, 'user': user}
    return render(request, 'hints.html', context)


def projects(request):
    hints = Hint.objects.all()[4:7]
    projs = Project.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'hints': hints, 'projects': projs, 'user': user}
    return render(request, 'projects.html', context=context)


def project1(request):
    questions = Test.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'questions': questions, 'user': user}
    return render(request, 'project1.html', context)


def project2(request):
    questions = Test.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'questions': questions, 'user': user}
    return render(request, 'project2.html', context)


def add_project(request):
    if request.user.is_superuser:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/dashboard')
        context = {'form': form}
        return render(request, 'addProject.html', context)
    else:
        return redirect('dashboard')


def exams(request):
    user = AppUser.objects.filter(user=request.user).get()
    if request.method == 'POST':
        print(request.POST)
        questions = Test.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        context = {'score': score, 'time': request.POST.get('timer'), 'correct': correct, 'wrong': wrong,
                   'percent': percent, 'total': total, 'user': user}
        return render(request, 'outcome.html', context)
    else:
        qs = Test.objects.all()
        context = {'questions': qs, 'user': user}
        return render(request, 'exams.html', context)


def profile(request):
    tutorials = Tutorial.objects.all()[2:5]
    user = AppUser.objects.filter(user=request.user).get()
    context = {'tutorials': tutorials, 'user': user}
    return render(request, 'profile.html', context=context)


def users_list(request):
    usrs = AppUser.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'users': usrs, 'user': user}
    return render(request, 'users.html', context=context)


def links(request):
    lins = Link.objects.all()
    user = AppUser.objects.filter(user=request.user).get()
    context = {'user': user, 'links': lins}
    return render(request, 'links.html', context=context)