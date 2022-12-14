import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import AddQuestionForm, NewUserForm, AddHintForm, AddLinkForm, AddTutorialForm
from .models import Tutorial, AppUser, Hint, Project, Test, Link
from django.contrib import messages
# Create your views here.


def dashboard(request):
    usrs = AppUser.objects.all()[5:9]
    lnks = Link.objects.all()[:5]
    tutorials = Tutorial.objects.all()[:3]
    hnts = Hint.objects.all()[2:5]
    context = {
        'date': datetime.datetime.now(),
        "tutorials": tutorials,
        'links': lnks,
        'hints': hnts,
        'user': request.user,
        'users': usrs
    }
    return render(request, 'dashboard.html', context=context)


def lectures(request):
    tutorials = Tutorial.objects.all()
    context = {'tutorials': tutorials, 'user': request.user}
    return render(request, 'lectures.html', context)


def hints(request):
    hnts = Hint.objects.all()
    context = {'hints': hnts, 'user': request.user}
    return render(request, 'hints.html', context)


def projects(request):
    hnts = Hint.objects.all()[4:7]
    projs = Project.objects.all()
    context = {'hints': hnts, 'projects': projs, 'user': request.user}
    return render(request, 'projects.html', context=context)


def project1(request):
    questions = Test.objects.all()[:5]
    if request.method == 'POST':
        print(request.POST)
        questions = Test.objects.all()[:5]
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
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'user': request.user
        }
        return render(request, 'outcome.html', context)
    else:
        context = {'questions': questions, 'user': request.user}
        return render(request, 'project1.html', context)


def project2(request):
    questions = Test.objects.all()[5:10]
    if request.method == 'POST':
        print(request.POST)
        questions = Test.objects.all()[5:10]
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
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'user': request.user
        }
        return render(request, 'outcome.html', context)
    else:
        context = {'questions': questions, 'user': request.user}
        return render(request, 'project2.html', context)


def add_hint(request):
    if request.user.is_superuser:
        form = AddHintForm()
        if request.method == 'POST':
            form = AddHintForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/hints')
        context = {'form': form}
        return render(request, 'addHint.html', context)
    else:
        return redirect('dashboard')


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


def add_tutorial(request):
    if request.user.is_superuser:
        form = AddTutorialForm()
        if request.method == 'POST':
            form = AddTutorialForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/tutorials')
        context = {'form': form}
        return render(request, 'addTutorial.html', context)
    else:
        return redirect('dashboard')


def add_link(request):
    if request.user.is_superuser:
        form = AddLinkForm()
        if request.method == 'POST':
            form = AddLinkForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/links')
        context = {'form': form}
        return render(request, 'addLink.html', context)
    else:
        return redirect('dashboard')


def exams(request):
    lnks = Link.objects.all()[3:6]
    hnts = Hint.objects.all()[:3]
    context = {'user': request.user, 'links': lnks, 'hints': hnts}
    return render(request, 'exams.html', context)


def exam(request):
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
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'user': request.user
        }
        return render(request, 'outcome.html', context)
    else:
        qs = Test.objects.all()
        context = {'questions': qs, 'user': request.user}
        return render(request, 'exam.html', context)


def profile(request):
    tutorials = Tutorial.objects.all()[2:5]
    context = {'tutorials': tutorials, 'user': request.user}
    return render(request, 'profile.html', context=context)


def users_list(request):
    usrs = AppUser.objects.all()
    users1 = User.objects.all()
    context = {'users': usrs, 'user': request.user, 'users1': users1}
    return render(request, 'users.html', context=context)


def links(request):
    lnks = Link.objects.all()
    context = {'user': request.user, 'links': lnks}
    return render(request, 'links.html', context=context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("dashboard")
        messages.error(request, "Unsuccessful registration. Invalid data provided")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out!")
    return redirect("dashboard")