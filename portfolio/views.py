from django.shortcuts import render

from portfolio.models import Project, Programmer


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
    return render(request, 'portfolio/projects.html',{
        'projects': Project.objects.all()
    })


def darkMode_page_view(request):
    return render(request, 'portfolio/dark-mode.html')
