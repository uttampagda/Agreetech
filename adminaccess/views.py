from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, auth
from .form import *
from .models import *

farm_id_g = None
farmer_id_g = None
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


def farmer_details(request):
    if request.method == 'POST':
        print("farmer_details",len(request.GET))
        farmer_id = request.POST.get('farmer_id')
        farm_info = Farm_info.objects.filter(farmer_id=farmer_id)
        farmer_info = Farmer.objects.filter(id=farmer_id)[0]
        data = {'farmer': farmer_id,
                'farm_info': farm_info,
                'farmer_info': farmer_info,
                }
        return render(request, 'forms/farmer_details.html', data)

def farm_info_reg(request):
    if request.method == 'POST':
        print('farm_info_reg',len(request.GET))
        farmer_id = request.POST.get('farmer_id')
        form = Farm_info_Form(request.POST, request.FILES)
        data = {'farmer_id': farmer_id}
        if form.is_valid() and form['farm_nick_name'].value()!=None:
            print("nick_name",form['farm_nick_name'].value())
            form.save()
            return render(request, 'forms/farm_info_reg.html', data)
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
        print("post")
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
        planting_history = Planting.objects.filter(farm_id=farm_id)
        data = {
            'farm_id': farm_id,
            'farmer_id': farmer_id,
            'planting_history': planting_history,
        }
        if form.is_valid():
            form.save()
            request.session['farm_id'] = farm_id
            return redirect('planting')
            # return render(request, 'forms/planting_reg.html',data)
    farmer_id = request.session['farmer_id']
    farm_id = request.session['farm_id']
    planting_history = Planting.objects.filter(farm_id=farm_id)
    data = {
        'farm_id': farm_id,
        'farmer_id': farmer_id,
        'planting_history': planting_history,
    }
    return render(request, 'forms/planting_reg.html', data)
    
def planting(request):
    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')
        farm_id = request.POST.get('farm_id')
        planting_history = Planting.objects.filter(farm_id=farm_id)
        data = {
            'planting_history': planting_history,
            'farmer_id': farmer_id,
            'farm_id': farm_id,
        }
        request.session['farmer_id'] = farmer_id
        request.session['farm_id'] = farm_id
        return render(request, 'forms/planting.html', data)
    else:
        farm_id = request.session['farm_id']
        print(farm_id)
        planting_history = Planting.objects.filter(farm_id=farm_id)
        data = {
            'planting_history': planting_history,
            'farm_id': farm_id,
        }
        return render(request, 'forms/planting.html', data)

def harvesting(request):
    if request.method == 'POST':
        print("Postttttt")
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


