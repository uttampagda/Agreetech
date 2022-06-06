from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, auth

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
    return render(request, 'dashboard/dashboard.html')

def permission_denied(request):
    return render(request, 'auth/403.html')


@login_required(login_url='login')
@permission_required('is_staff','403')
def createuser(request):
        if request.method == 'POST':
            number = request.POST['number']
            name = request.POST['name']
            group = request.POST['group']
            pass1 = request.POST['password1']
            pass2 = request.POST['password2']
            if group == 'Admin':
                is_staff = 1
            else:
                is_staff = 0
            if pass1 == pass2:
                user = User.objects.create_user(number, name, pass1,is_staff=is_staff)
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