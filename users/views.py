from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import RegisterForm

User = get_user_model()

def register(request):
    """Register page"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register_user.html', {'form': form})

def login_view(request):
    """Log in page"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login_user.html')

def logout_view(request):
    """Log out function"""
    logout(request)
    return redirect('home')