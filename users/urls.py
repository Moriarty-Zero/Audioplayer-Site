from .views import register, login_view, logout_view
from django.urls import path

urlpatterns = [
    #register page
    path('register/', register, name='register'),

    #log in page
    path('login/', login_view, name='login'),

    #log out page
    path('logout/', logout_view, name='logout'),
]