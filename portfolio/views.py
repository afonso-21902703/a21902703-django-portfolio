from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from portfolio.models import Project, Programmer, Lab, Technologies, News, Patterns


def home_page_view(request):
    aboutMeItems = {
        'Degree': ['Management IT'],
        'Education': ['Management IT'],
        'Skills': ['Java', 'JavaScript/HTML/CSS', 'Swift', 'Python'],
        'Hobbies': ['Video Games', 'Sports'],
        'Professional Experience': ['iOS Developer at NextReality']
    }
    return render(request, 'portfolio/home.html', {
        'aboutMeItems': aboutMeItems,
    })


def projects_page_view(request):
    s = ', '
    return render(request, 'portfolio/projects.html', {
        'projects': Project.objects.all(),
        's': s
    })


def darkMode_page_view(request):
    return render(request, 'portfolio/dark-mode.html')


def header_view(request):
    return render(request, 'portfolio/header.html')


def pw_view(request):
    return render(request, 'portfolio/pw.html', {
        'labs': Lab.objects.all(),
        'Technologies': Technologies.objects.all(),
        'News': News.objects.all()
    })


def about_view(request):
    used_tec = Technologies.objects.filter(usedInWeb=True)
    return render(request, 'portfolio/about.html', {
        'usedTec': used_tec,
        'patterns': Patterns.objects.all()
    })


def footer_view(request):
    return render(request, 'portfolio/footer.html')


def blog_view(request):
    return render(request, 'portfolio/blog.html')


def contact_view(request):
    return render(request, 'portfolio/contact.html')
