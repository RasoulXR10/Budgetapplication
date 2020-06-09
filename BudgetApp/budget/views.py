from django.shortcuts import render
from django.http import HttpResponse

projects = [
    {
        'author': 'rasoul',
        'title': 'Budget Project 1',
        'description': 'First project description',
        'date_created': 'Jun 9, 2020'
    },
    {
        'author': 'pouria',
        'title': 'Budget Project 2',
        'description': 'Second project description',
        'date_created': 'Jun 9, 2020'
    },
    {
        'author': 'rasoul',
        'title': 'Budget Project 1',
        'description': 'First project description',
        'date_created': 'Jun 9, 2020'
    },
    {
        'author': 'pouria',
        'title': 'Budget Project 2',
        'description': 'Second project description',
        'date_created': 'Jun 9, 2020'
    },
    {
        'author': 'rasoul',
        'title': 'Budget Project 1',
        'description': 'First project description',
        'date_created': 'Jun 9, 2020'
    },
    {
        'author': 'pouria',
        'title': 'Budget Project 2',
        'description': 'Second project description',
        'date_created': 'Jun 9, 2020'
    },
]


def home(request):
    content = {
        'projects': projects,
    }
    return render(request, 'budget/home.html', content)


def profile(request):
    return render(request, 'budget/profile.html', {'title': 'Profile'})
