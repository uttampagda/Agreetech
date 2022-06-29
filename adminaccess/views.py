from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, auth
from .form import *
from .models import *


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


def farmers(request):
    farmers = Farmer.objects.all()
    return render(request, 'forms/farmers.html', {'farmers':farmers})


def farmer_registration(request):
    if request.method == 'POST':    
        form = Farmer_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('farmers')
    else:
        form = Farmer_Form()
    return render(request, 'forms/farmer_registration.html')

def farm_info_reg(request, farmer_id):
    if request.method == 'POST':
        form = Farm_info_Form(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(f'/farmer_details/{farmer_id}')
    else:
        form = Farm_info_Form()
    data = {'farmer_id':farmer_id}
    return render(request, 'forms/farm_info_reg.html', data)

def farm_info(request):
    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')
        farm_id = request.POST.get('farm_id')
        farm_info = Farm_info.objects.filter(id=farm_id)[0]
        planting_history = Planting.objects.filter(id=farm_id)
        data = {
            'farm': farm_info,
            'planting_history': planting_history,
        }
        return render(request, 'forms/farm_info.html',data)
    else:
        return render(request, 'auth/403.html')




def soil_test(request):
    if request.method == 'POST':
        form = Soil_test_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Soil_test')
    else:
        form = Soil_test_Form()
    return render(request, 'forms/soil_test.html')

def planting_reg(request):
    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')
        farm_id = request.POST.get('farm_id')
        form = Planting_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Planting')
        data = {
            'farm_id' : farm_id,
            'farmer_id' : farmer_id,
        }
        return render(request, 'forms/planting_reg.html',data)

def harvesting(request):
    if request.method == 'POST':
        form = Harvesting_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Harvesting')
    else:
        form = Harvesting_Form()
    return render(request, 'forms/harvesting.html')


def crop_selling(request):
    if request.method == 'POST':
        form = Crop_selling_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Crop_selling')
    else:
        form = Crop_selling_Form()
    return render(request, 'forms/crop_selling.html')

def fertilizer(request):
    if request.method == 'POST':
        form = Fertilizer_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Fertilizer')
    else:
        form = Fertilizer_Form()
    return render(request, 'forms/fertilizer.html')

def water_irrigation(request):
    if request.method == 'POST':
        form = Water_irrigation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Water_irrigation')
    else:
        form = Water_irrigation_Form()
    return render(request, 'forms/water_irrigation.html')

def pesticide(request):
    if request.method == 'POST':
        form = Pesticide_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Pesticide')
    else:
        form = Pesticide_Form()
    return render(request, 'forms/pesticide.html')


def view_farmer(request, Id):
    farmer = Farmer.objects.filter(id = Id)[0]
    farm_info = Farm_info.objects.filter(farmer_id = Id)
    print(farm_info)    
    data = {'farmer':farmer, 'farm_info':farm_info}
    return render(request, 'forms/farmer_details.html',data)