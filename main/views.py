from django.shortcuts import render

def index(request):
    '''Main welcome page'''
    return render(request, 'main/index.html')

def about(request):
    '''Page about me'''
    return render(request, 'main/about.html')