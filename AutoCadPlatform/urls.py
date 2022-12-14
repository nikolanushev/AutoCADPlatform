"""AutoCadPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AutoCadApp.views import dashboard, lectures, projects, exams, profile, hints, project1, project2, add_project, \
    users_list, links, exam, register_request, login_request, logout_request, add_hint, add_tutorial, add_link
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('register', register_request, name="register"),
                  path('login', login_request, name="login"),
                  path('logout', logout_request, name="logout"),
                  path('', dashboard, name="dashboard"),
                  path('dashboard/', dashboard, name="dashboard"),
                  path('tutorials/', lectures, name="lectures"),
                  path('addTutorial/', add_tutorial, name="add_tutorial"),
                  path('project1/', project1, name="project1"),
                  path('project2/', project2, name="project2"),
                  path('projects/', projects, name="projects"),
                  path('addProject/', add_project, name="add_project"),
                  path('tests/', exams, name="exams"),
                  path('test/', exam, name="exam"),
                  path('profile/', profile, name="profile"),
                  path('hints/', hints, name="hints"),
                  path('addHint/', add_hint, name="add_hint"),
                  path('users/', users_list, name="users_list"),
                  path('links/', links, name="links"),
                  path('addLink/', add_link, name="add_link")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
