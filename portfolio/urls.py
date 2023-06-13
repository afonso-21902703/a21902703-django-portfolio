from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('projects', views.projects_page_view, name='projects'),
    path('dark-mode', views.darkMode_page_view, name='dark-mode'),
    path('header', views.header_view, name='header'),
    path('pw', views.pw_view, name='pw'),
    path('about', views.about_view, name='about'),
    path('footer', views.footer_view, name='footer')
]
