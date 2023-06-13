from django.shortcuts import render
from datetime import datetime

from portfolio.models import Project, Programmer, Lab, Technologies, News


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
    return render(request, 'portfolio/about.html')


def footer_view(request):
    data: datetime.now()
    return render(request, 'portfolio/footer.html', {
        'date': data
    })
