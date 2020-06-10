from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def home(request):
    content = {
        'projects': Project.objects.all(),
    }
    return render(request, 'budget/home.html', content)


def profile(request):
    return render(request, 'budget/profile.html', {'title': 'Profile'})


def add_project(request):
    return render(request, 'budget/add-project.html', {'title': 'Add Project'})
