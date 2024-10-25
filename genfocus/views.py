from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from .models import Profile

# Create your views here.

def home(request):
    total_users = User.objects.count()
    context = {'total_users': total_users}
    return render(request, 'index.html', context)

def login(request):
    if request.user.is_authenticated:
        return render(request, 'usergen/main.html')
    else:
        if request.method == 'GET':
            return render(request, 'registration/login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('passsword')

            user = authenticate(username=username, password=password)

            if user:
                login_django(request, user)
                return render(request, 'usergen/main.html')


        

def signup(request):
    if request.user.is_authenticated:
        return render(request, 'usergen/main.html')
    else:
        if request.method == 'GET':
            return render(request, 'registration/signup.html')
        else:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            cpf = request.POST.get('cpf')
            civil_state = request.POST.get('civil_state')

            user = User.objects.filter(username=username).first()

            if user:
                return render(request, 'registration/login.html')
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name, last_name=lastname)
            user.save()
            userprofile = Profile.objects.create(cpf=cpf, civil_state=civil_state)
            userprofile.save()
            login_django(request, user)
            return render(request, 'usergen/main.html')

@login_required
def logout(request):
    logout_django(request, request.user)
    return render(request, 'index.html')

@login_required
def usergen(request):
    return render(request, 'usergen/main.html')

@login_required
def users_list(request):
    users = {'users': User.objects.all()}
    return render(request, 'usergen/userslist.html', users)
