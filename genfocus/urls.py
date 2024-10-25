from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('usergen', views.usergen, name='usergen'),
    path('signup', views.signup, name='signup')
]