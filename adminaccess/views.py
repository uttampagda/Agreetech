from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, auth
from .form import *
from .models import *
from datetime import datetime


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


def farmer_details(request,farmer_id):
    if request.method == 'POST':
        # print("farmer_details",len(request.GET))
        # farmer_id = request.POST.get('farmer_id')
        farm_info = Farm_info.objects.filter(farmer_id=farmer_id)
        farmer_info = Farmer.objects.filter(id=farmer_id)[0]
        data = {'farmer_id': farmer_id,
                'farm_info': farm_info,
                'farmer_info': farmer_info,
                }
        request.session['farmer_id'] = farmer_id
        print("farmer_details        farmer_id",farmer_id)
        return render(request, 'forms/farmer_details.html', data)
    else:
        # farmer_id = request.session['farmer_id']
        print("farmer_details else farmer_id",farmer_id)
        farm_info = Farm_info.objects.filter(farmer_id=farmer_id)
        farmer_info = Farmer.objects.filter(id=farmer_id)[0]
        data = {'farmer_id': farmer_id,
                'farm_info': farm_info,
                'farmer_info': farmer_info,
                }
        request.session['farmer_id'] = farmer_id
        return render(request, 'forms/farmer_details.html', data)

def farm_info_reg(request):
    farmer_id = request.session['farmer_id']
    if request.method == 'POST':
        form = Farm_info_Form(request.POST, request.FILES)
        if form.is_valid() and form['farm_nick_name'].value()!=None:
            form.save()
            request.session['farmer_id'] = farmer_id
            print("farm_info if save farmer_id", farmer_id)
            return redirect('farmer_details',farmer_id)
    else:
        farmer_id = request.session['farmer_id']
    data = {'farmer_id': farmer_id}
    return render(request, 'forms/farm_info_reg.html', data)


def farm_info(request,farm_id):
    farmer_id = request.session['farmer_id']
    farm_info = Farm_info.objects.filter(id=farm_id)[0]
    planting_history = Planting.objects.filter(farm_id=farm_id)
    data = {
            'farmer' : farm_info.farmer_id,
            'farmer_id' : farmer_id,
            'farm': farm_info,
            'planting_history': planting_history,
        }
    request.session['farmer_id'] = farmer_id
    request.session['farm_id'] = farm_id
    return render(request, 'forms/farm_info.html',data)

def soil_test(request):
    farmer_id = request.session['farmer_id']
    farm_id = request.session['farm_id']

    if request.method == 'POST':
        farmer_id = request.session['farmer_id']
        form = Soil_test_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('soil_test')
    else:
        form = Soil_test_Form()
    data={
        'farmer_id':farmer_id,
        'farm_id':farm_id,
    }
    return render(request, 'forms/soil_test.html',data)

def planting_reg(request):
    default_plant_name = dict(Default_plant_name.objects.values())
    default_plant_seed_name = Default_plant_seed_name.objects.values()
    print(default_plant_name, default_plant_seed_name)
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
            return redirect(f'/farm_info/farm_id={farm_id}')
            # return render(request, 'forms/planting_reg.html',data)
    farmer_id = request.session['farmer_id']
    farm_id = request.session['farm_id']
    planting_history = Planting.objects.filter(farm_id=farm_id)

    import json
    data = {
        'default_plant_name':json.dumps(default_plant_name),
        'default_plant_seed_name': default_plant_seed_name,
        'farm_id': farm_id,
        'farmer_id': farmer_id,
        'planting_history': planting_history,
    }
    return render(request, 'forms/planting_reg.html', data)

def planting(request,planting_id):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_history = Planting.objects.filter(id=planting_id)[0]
    fertilizer = Fertilizer.objects.filter(planting_id=planting_id)
    water_irrigation = Water_irrigation.objects.filter(planting_id=planting_id).values()
    pesticide = Pesticide.objects.filter(planting_id=planting_id).values()
    
    # Creating DateTime var for multiple use
    date_now=datetime.now().date()
    
    if planting_history.planting_time != None:
        time_from_planting = (date_now-planting_history.planting_time.date()).days
    else:
        time_from_planting = "No information provided"
    planting_history.time_from_planting = time_from_planting

    for fer in fertilizer:
       if fer.fertilizer_date != None:
           time_from_fertilizer = (date_now-fer.fertilizer_date.date()).days
       else:
           time_from_fertilizer = "No information provided"
       fer.time_from_fertilizer = time_from_fertilizer

    for water in water_irrigation:
       if water['water_irrigation_date'] != None:
           time_from_water_irrigation = (date_now-water['water_irrigation_date'].date()).days
       else:
           time_from_water_irrigation = "No information provided"
       water['time_from_water_irrigation'] = time_from_water_irrigation
    
    for pes in pesticide:
       if pes['pesticide_date'] != None:
           time_from_prestiside = (date_now-pes['pesticide_date'].date()).days
       else:
           time_from_prestiside = "No information provided"
       pes['time_from_prestiside'] = time_from_prestiside
    print('planting_history.farmer_id[0]',planting_history.farmer_id)
    data = {
        'farmer' : planting_history.farmer_id,
        'farm_id':farm_id,
        'planting_id': planting_id,
        'planting_history': planting_history,
        'fertilizer': fertilizer,
        'water_irrigation': water_irrigation,
        'pesticide': pesticide
    }
    request.session['farmer_id'] = farmer_id
    request.session['farm_id'] = farm_id
    request.session['planting_id'] = planting_id
    return render(request,'forms/planting.html',data)

def harvesting_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    if request.method == 'POST':
        form = Harvesting_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['farmer_id'] = farmer_id
            request.session['farm_id'] = farm_id
            request.session['planting_id'] = planting_id
            return redirect('harvesting_and_crop_selling')
    data = {
        'farm_id': farm_id,
        'farmer_id': farmer_id,
        'planting_id': planting_id,
    }
    return render(request, 'forms/harvesting_reg.html',data)


def crop_selling_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    if request.method == 'POST':
        form = Crop_selling_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['farmer_id'] = farmer_id
            request.session['farm_id'] = farm_id
            request.session['planting_id'] = planting_id
            return redirect('harvesting_and_crop_selling')
    data = {
        'farm_id':farm_id,
        'farmer_id':farmer_id,
        'planting_id': planting_id,
    }
    return render(request, 'forms/crop_selling_reg.html',data)

def harvesting_and_crop_selling(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    harvesting = Harvesting.objects.filter(planting_id=planting_id)
    crop_selling = Crop_selling.objects.filter(planting_id=planting_id)
    data = {
          'farmer_id': farmer_id,
          'farm_id': farm_id,
          'planting_id': planting_id,
          'harvesting': harvesting,
          'crop_selling': crop_selling,
      }
    request.session['farmer_id'] = farmer_id
    request.session['farm_id'] = farm_id
    request.session['planting_id'] = planting_id
    return render(request, 'forms/harvesting_and_selling.html',data)

def fertilizer_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    fertilizer_selection = Default_fertilizer.objects.values()
    if request.method == 'POST':
        form = Fertilizer_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #for review
            fertilizer = Default_fertilizer.objects.filter(fertilizer_name=form.data['fertilizer_name'])[0]
            total_review = fertilizer.total_review + int(form.data['review'])
            number_of_reviews = fertilizer.number_of_reviews + 1
            avarage_review = round( total_review / number_of_reviews, 1)
            print(total_review,number_of_reviews,avarage_review)
            fertilizer.total_review = total_review
            fertilizer.number_of_reviews = number_of_reviews
            fertilizer.avarage_review = avarage_review
            fertilizer.save()
            return redirect('planting',planting_id=planting_id)
    data = {
        'farmer_id' : farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
        'fertilizer_selection' : fertilizer_selection
    }
    return render(request, 'forms/fertilizer_reg.html',data)

def fertilizer_info(request, fertilizer_id):
    fertilizer = Fertilizer.objects.filter(id=fertilizer_id)[0]
    data = {
        'fertilizer':fertilizer,
        'farmer':fertilizer.farmer_id
    }
    return render(request, 'forms/fertilizer_info.html', data)

def water_irrigation_info(request, water_irrigation_id):
    water_irrigation = Water_irrigation.objects.filter(id=water_irrigation_id)[0]
    data = {
        'water_irrigation':water_irrigation,
        'farmer':water_irrigation.farmer_id
    }
    return render(request, 'forms/water_irrigation_info.html', data)

def pesticide_info(request, pesticide_id):
    pesticide = Pesticide.objects.filter(id=pesticide_id)[0]
    data = {
        'pesticide':pesticide,
        'farmer': pesticide.farmer_id
    }
    return render(request, 'forms/pesticide_info.html', data)  


def water_irrigation_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    if request.method == 'POST':
        form = Water_irrigation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('planting',planting_id=planting_id)

    data = {
        'farmer_id': farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
    }
    return render(request, 'forms/water_irrigation_reg.html',data)

def pesticide_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    if request.method == 'POST':
        form = Pesticide_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('planting',planting_id=planting_id)
    data = {
                'farmer_id': farmer_id,
                'farm_id': farm_id,
                'planting_id': planting_id,
            }
    return render(request, 'forms/pesticide_reg.html',data)

def search(request):
    farm_info = Farm_info.objects.values()
    farm = []
    for i in farm_info:
        if farm:
            for j in farm:
                if j['farmer_id'] == i['farmer_id']:
                    print(i['farmer_id'],j['farmer_id'])
                    j['farm_space'] += i['farm_space']
                else:
                    farm.append(i)
        else:
            farm.append(i)
    data = {'farm_info':farm}
    return render(request, 'forms/search.html', data)

def search_utm(request):
    farms = Farm_info.objects.all()
    farmers = Farmer.objects.all()
    temp_list = []
    for i in farms:
        temp_list.append([i.farmer_id,i.farm_space])
    temp_farmer_ids = []
    for i in range(len(temp_list)):
        temp_farmer_ids.append(temp_list[i][0])
    temp_farmer_ids = list(set(temp_farmer_ids))
    final_list = []
    f_list= []
    for i in farmers:
        for j in temp_farmer_ids:
            if i.id==j:
                f_list.append([j,i.name])
    for j,k in f_list:
        space=0
        for i in range(len(temp_list)):
            if temp_list[i][0] == j:
                space += temp_list[i][1]
        final_list.append([j, space,k])
    data = {
        'final_list': final_list,
        'farmers': farmers,
    }   
    return render(request, 'forms/search_utm.html',data)

def default_parameters(request):
    return render(request, 'Default_parameters/default_parameters.html')

def default_plant_name(request):
    plant_names = Default_plant_name.objects.all()
    # if request.method == 'POST':
    #     form = Default_plant_name_Form(request.POST)
    #     if form.is_valid():
    #         print("1st er",form.errors)
    #         print("1st valid")
    #         form.save()
    #         return redirect('default_plant_name')
    # if request.method == 'POST':
    #     form = Default_plant_seed_name_Form(request.POST)
    #     print(form['plant_name'].value(),form['seed_name'].value())
    #     print("2nd error",form.errors)
    #     if form.is_valid():
    #         print("2nd valid")
    #         form.save()
    #         return redirect('default_plant_name')
    # if request.method == 'POST':
    #     if request.POST.get('form_name')=='plant_reg':
    #         print('plant')
            
    #         form = Default_plant_name_Form(request.POST)
    #         if form.is_valid():
    #                 form.save()
    #                 return redirect('default_plant_name')
    #     if request.POST.get('form_name')=='seed_reg':
    #         print('seed')
            
    #         form = Default_plant_seed_name_Form(request.POST)
    #         if form.is_valid():
    #                 form.save()
    #                 return redirect('default_plant_name')
    data = {
        'plant_names' : plant_names
    }    
    return render(request, 'Default_parameters/default_plant_name_reg.html',data)
def add_default_plant_name(request):
    if request.method == 'POST':
        form = Default_plant_name_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('default_plant_name')

def select_default_plant_name(request):
    if request.method == 'POST':
        form = Default_plant_seed_name_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('default_plant_name')
        
def add_default_fertilizer(request):
    default_fertilizer = Default_fertilizer.objects.all()
    if request.method == 'POST':
        form = Default_fertilizer_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_default_fertilizer')
    data = {
        'default_fertilizer' : default_fertilizer
    }    
    return render(request, 'Default_parameters/default_fertilizer.html',data)

def add_default_pesticide(request):
    default_pesticide = Default_pesticide.objects.all()
    if request.method == 'POST':
        form = Default_pesticide_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_default_pesticide')
    data = {
        'default_pesticide' : default_pesticide
    }    
    return render(request, 'Default_parameters/default_pesticide.html',data)

def farmer_edit(request, farmer_id):
    farmer = Farmer.objects.get(id=farmer_id)
    farmers = Farmer.objects.filter(id=farmer_id)

    if request.method == 'POST':
        form = Farmer_Form(request.POST, instance=farmer)

        if form.is_valid():
            form.save()
            return redirect(f'/farmer_details/farmer_id={farmer_id}')
    
    return render(request, 'form_edit/farmer_edit.html', {'farmer':farmers})


def farm_edit(request, farm_id):
    farm = Farm_info.objects.get(id=farm_id)
    farms = Farm_info.objects.filter(id=farm_id)

    if request.method == 'POST':
        form = Farm_info_Form(request.POST, instance=farm)

        if form.is_valid():
            form.save()
            return redirect(f'/farm_info/farm_id={farm_id}')
    
    return render(request, 'form_edit/farm_edit.html', {'farms':farms})


def plant_edit(request, plant_id):
    plants = Planting.objects.filter(id=plant_id)
    plant = Planting.objects.get(id=plant_id)

    if request.method == 'POST':
        form = Planting_Form(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect(f'/planting/planting_id={plant_id}')
    
    return render(request, 'form_edit/planting_edit.html', {'plants':plants})


def fertilizer_edit(request, fertilizer_id):
    fertilizer = Fertilizer.objects.get(id=fertilizer_id)
    fertilizers = Fertilizer.objects.filter(id=fertilizer_id)

    if request.method == 'POST':
        form = Fertilizer_Form(request.POST, instance=fertilizer)

        if form.is_valid():
            form.save()
            return redirect(f'/fertilizer_info/fertilizer_id={fertilizer_id}')
    
    return render(request, 'form_edit/fertilizer_edit.html', {'fertilizers':fertilizers})


def water_irrigation_edit(request, water_irrigation_id):
    water_irrigation = Water_irrigation.objects.get(id=water_irrigation_id)
    water_irrigations = Water_irrigation.objects.filter(id=water_irrigation_id)

    if request.method == 'POST':
        form = Water_irrigation_Form(request.POST, instance=water_irrigation)

        if form.is_valid():
            form.save()
            return redirect(f'/water_irrigation_info/water_irrigation_id={water_irrigation_id}')
    
    return render(request, 'form_edit/water_irrigation_edit.html', {'water_irrigations':water_irrigations})


def pesticide_edit(request, pesticide_id):
    pesticide = Pesticide.objects.get(id=pesticide_id)
    pesticides = Pesticide.objects.filter(id=pesticide_id)

    if request.method == 'POST':
        form = Pesticide_Form(request.POST, instance=pesticide)

        if form.is_valid():
            form.save()
            return redirect(f'/pesticide_info/pesticide_id={pesticide_id}')
    
    return render(request, 'form_edit/pesticide_edit.html', {'pesticides':pesticides})

def fertilizer_stats(request,fertilizer_name):
    fertilizer = Fertilizer.objects.filter(fertilizer_name=fertilizer_name).order_by('create_date')
    print(fertilizer[0].id,fertilizer[0].fertilizer_name)
    print(fertilizer)
    data = {
        'fertilizer_name' : fertilizer[0].fertilizer_name,
        'fertilizer': fertilizer
    }
    return render(request,'stats/fertilizer_stats.html',data)