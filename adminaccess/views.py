from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, auth
from .form import Farmer_Form, Farm_info_Form, Soil_test_Form


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.warning(request, 'you are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'auth/login.html')

@login_required(login_url='login')
def dashboard(request):
    user = request.user.username
    data ={
        'user': user,
    }
    return render(request, 'dashboard/dashboard.html')

def permission_denied(request):
    return render(request, 'auth/403.html')


@login_required(login_url='login')
@permission_required('is_staff','403')
def createuser(request):
        if request.method == 'POST':
            email = request.POST['email']
            name = request.POST['name']
            group = request.POST['group']
            pass1 = request.POST['password1']
            pass2 = request.POST['password2']
            if group == 'Admin':
                is_staff = 1
            else:
                is_staff = 0
            if pass1 == pass2:
                user = User.objects.create_user(email, name, pass1,is_staff=is_staff)
                user.save()
                return redirect('dashboard')
        return render(request, 'auth/createuser.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


#======================================== Froms =========================================

def forms(request):
    return render(request, 'forms/forms.html')

def farmer_registration(request):
    return render(request, 'forms/farmer_registration.html')

def Farmer(request):
    if request.method == 'POST':
        form = Farmer_Form(request.POST, request.FILES)
        print("::::::::::::::::::::1")
        if form.is_valid():
            form.save()
            print("::::::::::::::::::::2")
            return redirect('Farmer')
    else:
        print("::::::::::::::::::::3")
        form = Farmer_Form()
    return render(request, 'forms/farmer.html')

def Farm_info(request):
    if request.method == 'POST':
        form = Farm_info_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Farm_info')
    else:
        form = Farm_info_Form()
    return render(request, 'forms/farm_info.html')

def Soil_test(request):
    if request.method == 'POST':
        form = Soil_test_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Soil_test')
    else:
        form = Soil_test_Form()
    return render(request, 'forms/soil_test.html')


