from django.urls import path
from . import  views

urlpatterns = [
    # Main welcome page
    path('', views.index, name='home'),

    # Page about me 
    path('about', views.about, name='about'),
]