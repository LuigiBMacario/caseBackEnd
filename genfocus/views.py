from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

@login_required
def usergen(request):
    return render(request, 'usergen.html')