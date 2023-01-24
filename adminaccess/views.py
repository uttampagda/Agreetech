from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, auth
from .form import *
from .models import *
from datetime import datetime
from django.core.exceptions import PermissionDenied

global cur_obj
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
    data = {
        'user': user,
    }
    return render(request, 'dashboard/dashboard.html')


def permission_denied(request):
    return render(request, 'auth/403.html')


def staff_permission(farmer_id=None, staff_type=None):
    if farmer_id == None:
        farmer_id = request.session['farmer_id']
    farmer = Farmer.objects.filter(id=farmer_id)[0]
    if farmer.is_access or staff_type:
        return True
    else:
        return False


@login_required(login_url='login')
def createuser(request):
    if staff_permission:
        pass
    else:
        return redirect('403')
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
            user = User.objects.create_user(
                email, name, pass1, is_staff=is_staff)
            user.save()

            return redirect('dashboard')
    return render(request, 'auth/createuser.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


# ======================================== Froms =========================================

def forms(request):
    return render(request, 'forms/forms.html')


def farmers(request):
    farmers = Farmer.objects.all()

    return render(request, 'forms/farmers.html', {'farmers': farmers})


@permission_required('is_staff', '403')
def farmer_registration(request):
    if request.method == 'POST':
        form = Farmer_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('farmers')
    else:
        form = Farmer_Form()
    return render(request, 'forms/farmer_registration.html')


def farmer_details(request, farmer_id):
    if staff_permission(farmer_id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    if request.method == 'POST':
        farm_info = Farm_info.objects.filter(farmer_id=farmer_id)
        farmer_info = Farmer.objects.filter(id=farmer_id)[0]
        data = {'farmer_id': farmer_id,
                'farm_info': farm_info,
                'farmer_info': farmer_info,
                }
        request.session['farmer_id'] = farmer_id
        return render(request, 'forms/farmer_details.html', data)
    else:
        farm_info = Farm_info.objects.filter(farmer_id=farmer_id)
        farmer_info = Farmer.objects.filter(id=farmer_id)[0]
        total_farm_space = 0
        for farm in farm_info:
            try:
                total_farm_space += farm.farm_space
            except:
                pass
        data = {'farmer_id': farmer_id,
                'farm_info': farm_info,
                'farmer_info': farmer_info,
                'total_farm_space':total_farm_space,
                }
        request.session['farmer_id'] = farmer_id
        return render(request, 'forms/farmer_details.html', data)


def farm_info_reg(request):
    farmer_id = request.session['farmer_id']
    if request.method == 'POST':
        form = Farm_info_Form(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid() and form['farm_nick_name'].value() != None:
            form.save()
            request.session['farmer_id'] = farmer_id
            print("farm_info if save farmer_id", farmer_id)
            return redirect('farmer_details', farmer_id)
    else:
        farmer_id = request.session['farmer_id']
    data = {'farmer_id': farmer_id}
    return render(request, 'forms/farm_info_reg.html', data)


def farm_info(request, farm_id):
    farmer_id = request.session['farmer_id']
    if staff_permission(farmer_id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    farm_info = Farm_info.objects.filter(id=farm_id)[0]
    planting_history = Planting.objects.filter(farm_id=farm_id)
    soil_test = Soil_test.objects.filter(farm_id=farm_id).values()
    water_test = Water_test.objects.filter(farm_id=farm_id).values()
    global cur_obj
    cur_obj = farm_info
    data = {
        'farmer': farm_info.farmer_id,
        'farmer_id': farmer_id,
        'farm': farm_info,
        'planting_history': planting_history,
        'soil_test': soil_test,
        'water_test':water_test,
    }
    request.session['farmer_id'] = farmer_id
    request.session['farm_id'] = farm_id
    return render(request, 'forms/farm_info.html', data)


def soil_test(request):
    farmer_id = request.session['farmer_id']
    farm_id = request.session['farm_id']

    if request.method == 'POST':
        farmer_id = request.session['farmer_id']
        form = Soil_test_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f'/farm_info/farm_id={farm_id}')
    else:
        form = Soil_test_Form()
    data = {
        'farmer_id': farmer_id,
        'farm_id': farm_id,
    }
    return render(request, 'forms/soil_test.html', data)


def soil_test_info(request, id):
    soil_test = Soil_test.objects.filter(id=id)[0]
    farm_id = request.session['farm_id']
    if staff_permission(soil_test.farmer_id.id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    global cur_obj
    cur_obj = soil_test
    data = {
        'soil_test': soil_test,
        'farmer': soil_test.farmer_id,
        'farm_id': farm_id,
    }
    return render(request, 'forms/soil_test_info.html', data)

def water_test(request):
    farmer_id = request.session['farmer_id']
    farm_id = request.session['farm_id']

    if request.method == 'POST':
        farmer_id = request.session['farmer_id']
        form = Water_test_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f'/farm_info/farm_id={farm_id}')
    else:
        form = Water_test_Form()
    data = {
        'farmer_id': farmer_id,
        'farm_id': farm_id,
    }
    return render(request, 'forms/water_test.html', data)

def soil_test_edit(request, soil_test_id):
    soil_test = Soil_test.objects.get(id=soil_test_id)
    soil_test_data = Soil_test.objects.filter(id=soil_test_id)

    if request.method == 'POST':
        form = Soil_test_Form(request.POST, instance=soil_test)

        if form.is_valid():
            form.save()
            return redirect(f'/farm_info/farm_id={soil_test_id}')

    return render(request, 'form_edit/soil_test_edit.html', {'soil_test': soil_test_data})


def water_test_info(request, id):
    water_test = Water_test.objects.filter(id=id)[0]
    farm_id = request.session['farm_id']
    if staff_permission(water_test.farmer_id.id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    global cur_obj
    cur_obj = water_test
    data = {
        'water_test': water_test,
        'farmer': water_test.farmer_id,
        'farm_id': farm_id,
    }
    return render(request, 'forms/water_test_info.html', data)

def water_test_edit(request, water_test_id):
    water_test = Water_test.objects.get(id=water_test_id)
    water_test_data = Water_test.objects.filter(id=water_test_id)

    if request.method == 'POST':
        form = Water_test_Form(request.POST, instance=water_test)

        if form.is_valid():
            form.save()
            return redirect(f'/farm_info/farm_id={water_test_id}')

    return render(request, 'form_edit/water_test_edit.html', {'water_test': water_test_data})

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
            return redirect(f'/farm_info/farm_id={farm_id}')
            # return render(request, 'forms/planting_reg.html',data)
    farmer_id = request.session['farmer_id']
    farm_id = request.session['farm_id']
    planting_history = Planting.objects.filter(farm_id=farm_id)

    default_plant_name = list(Default_plant_name.objects.values())
    default_plant_seed_name_1 = Default_plant_seed_name.objects.all()
    default_plant_seed_name = []
    for plant_seed_name in default_plant_seed_name_1:
        default_plant_seed_name_dict = {}
        default_plant_seed_name_dict['plant_name'] = plant_seed_name.plant_name.plant_name
        default_plant_seed_name_dict['plant'] = plant_seed_name.seed_name
        default_plant_seed_name.append(default_plant_seed_name_dict)
    data = {
        'default_plant_name': default_plant_name,
        'default_plant_seed_name': default_plant_seed_name,
        'farm_id': farm_id,
        'farmer_id': farmer_id,
        'planting_history': planting_history,
    }
    return render(request, 'forms/planting_reg.html', data)


def planting(request, planting_id):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    if staff_permission(farmer_id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    planting_history = Planting.objects.filter(id=planting_id)[0]
    fertilizer = Fertilizer.objects.filter(planting_id=planting_id)
    water_irrigation = Water_irrigation.objects.filter(
        planting_id=planting_id).values()
    pesticide = Pesticide.objects.filter(planting_id=planting_id).values()
    crop_selling = Crop_selling.objects.filter(
        planting_id=planting_id).values()
    harvesting = Harvesting.objects.filter(planting_id=planting_id).values()
    pesticide_dose = Pesticide_dose.objects.filter(
        planting_id=planting_id).values()

    # Creating DateTime var for multiple use
    date_now = datetime.now().date()

    if planting_history.planting_time != None:
        time_from_planting = (
            date_now-planting_history.planting_time.date()).days
    else:
        time_from_planting = "No information provided"
    planting_history.time_from_planting = time_from_planting

    for fer in fertilizer:
        if fer.planting_id.planting_time != None:
            time_from_fertilizer = (
                date_now-fer.planting_id.planting_time.date()).days
        else:
            time_from_fertilizer = "No information provided"
        fer.time_from_fertilizer = time_from_fertilizer

    for water in water_irrigation:
        if water['water_irrigation_date'] != None:
            time_from_water_irrigation = (
                date_now-water['water_irrigation_date'].date()).days
        else:
            time_from_water_irrigation = "No information provided"
        water['time_from_water_irrigation'] = time_from_water_irrigation

    for pes in pesticide:
        if pes['pesticide_date'] != None:
            time_from_prestiside = (date_now-pes['pesticide_date'].date()).days
        else:
            time_from_prestiside = "No information provided"
        pes['time_from_prestiside'] = time_from_prestiside
    global cur_obj
    cur_obj = planting_history
    data = {
        'farmer': planting_history.farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
        'planting_history': planting_history,
        'fertilizer': fertilizer,
        'water_irrigation': water_irrigation,
        'pesticide': pesticide,
        'harvesting': harvesting,
        'crop_selling': crop_selling,
        'pesticide_dose': pesticide_dose
    }
    request.session['farmer_id'] = farmer_id
    request.session['farm_id'] = farm_id
    request.session['planting_id'] = planting_id
    return render(request, 'forms/planting.html', data)


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
            # return redirect('harvesting_and_crop_selling')
            return redirect('planting', planting_id=planting_id)
    data = {
        'farm_id': farm_id,
        'farmer_id': farmer_id,
        'planting_id': planting_id,
    }
    return render(request, 'forms/harvesting_reg.html', data)


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
            # return redirect('harvesting_and_crop_selling')
            return redirect('planting', planting_id=planting_id)
    data = {
        'farm_id': farm_id,
        'farmer_id': farmer_id,
        'planting_id': planting_id,
    }
    return render(request, 'forms/crop_selling_reg.html', data)


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
    return render(request, 'forms/harvesting_and_selling.html', data)


def fertilizer_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']

    if staff_permission(farmer_id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')

    fertilizer_selection = Default_fertilizer.objects.values()
    if request.method == 'POST':
        form = Fertilizer_Form(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            # for review
            fertilizer = Default_fertilizer.objects.filter(
                fertilizer_name=form.data['fertilizer_name'])[0]
            try:
                total_review = fertilizer.total_review + \
                    int(form.data['rating'])
                number_of_reviews = fertilizer.number_of_reviews + 1
                avarage_review = round(total_review / number_of_reviews, 1)
                fertilizer.total_review = total_review
                fertilizer.number_of_reviews = number_of_reviews
                fertilizer.avarage_review = avarage_review
                fertilizer.save()
            except:
                pass

            # calculating => fertilizer_days_from_planting
            planting = Planting.objects.filter(id=planting_id)[0]
            fertilizer_days_from_planting = (datetime.fromisoformat(
                form.data['fertilizer_date']).date()-planting.planting_time.date()).days
            form_save.fertilizer_days_from_planting = fertilizer_days_from_planting
            form_save.save()
            return redirect('planting', planting_id=planting_id)
    data = {
        'farmer_id': farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
        'fertilizer_selection': fertilizer_selection
    }
    return render(request, 'forms/fertilizer_reg.html', data)


def fertilizer_info(request, fertilizer_id):
    fertilizer = Fertilizer.objects.filter(id=fertilizer_id)[0]
    if staff_permission(fertilizer.farmer_id.id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    data = {
        'fertilizer': fertilizer,
        'farmer': fertilizer.farmer_id
    }
    return render(request, 'forms/fertilizer_info.html', data)


def water_irrigation_info(request, water_irrigation_id):
    water_irrigation = Water_irrigation.objects.filter(
        id=water_irrigation_id)[0]
    if staff_permission(water_irrigation.farmer_id.id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    data = {
        'water_irrigation': water_irrigation,
        'farmer': water_irrigation.farmer_id
    }
    return render(request, 'forms/water_irrigation_info.html', data)



def pesticide_info(request, pesticide_id):
    pesticide = Pesticide.objects.filter(id=pesticide_id)[0]
    if staff_permission(pesticide.farmer_id.id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    global cur_obj
    cur_obj = pesticide
    data = {
        'pesticide': pesticide,
        'farmer': pesticide.farmer_id,
        'cur_obj': cur_obj,
    }
    return render(request, 'forms/pesticide_info.html', data)

def delete_record(request):
    record = cur_obj.__class__.objects.filter(id=cur_obj.id)[0]
    data = {'record': vars(record)}
    return render(request,'extras/delete.html',data)

def harvesting_info(request, id):
    harvesting = Harvesting.objects.filter(id=id)[0]
    if staff_permission(harvesting.farmer_id.id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    global cur_obj
    cur_obj = harvesting
    data = {
        'harvesting': harvesting,
        'farmer': harvesting.farmer_id
    }
    return render(request, 'forms/harvesting_info.html', data)


def crop_selling_info(request, id):
    crop_selling = Crop_selling.objects.filter(id=id)[0]
    if staff_permission(crop_selling.farmer_id.id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    global cur_obj
    cur_obj = crop_selling
    data = {
        'crop_selling': crop_selling,
        'farmer': crop_selling.farmer_id
    }
    return render(request, 'forms/crop_selling_info.html', data)


def water_irrigation_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    if request.method == 'POST':
        form = Water_irrigation_Form(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            planting = Planting.objects.filter(id=planting_id)[0]
            water_date_from_planting = (datetime.fromisoformat(
                form.data['water_irrigation_date']).date()-planting.planting_time.date()).days
            form_save.water_date_from_planting = water_date_from_planting
            form_save.save()
            return redirect('planting', planting_id=planting_id)

    data = {
        'farmer_id': farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
    }
    return render(request, 'forms/water_irrigation_reg.html', data)


def pesticide_dose_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    if request.method == 'POST':
        form = Pesticide_dose_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('planting', planting_id=planting_id)
    data = {
        'farmer_id': farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
    }
    return render(request, 'forms/pesticide_dose_reg.html', data)


def pesticide_dose_info(request, dose_id):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    dose = Pesticide_dose.objects.filter(id=dose_id)[0]
    pesticide = Pesticide.objects.filter(dose_id=dose_id)
    global cur_obj
    cur_obj = dose
    data = {
        'farmer_id': farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
        'dose': dose,
        'pesticide': pesticide,
    }
    request.session['dose_id'] = dose.id
    return render(request, 'forms/pesticide_dose_info.html', data)


def pesticide_reg(request):
    farm_id = request.session['farm_id']
    farmer_id = request.session['farmer_id']
    planting_id = request.session['planting_id']
    dose_id = request.session['dose_id']
    pesticide_selection = Default_pesticide.objects.all()
    if request.method == 'POST':
        form = Pesticide_Form(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form_save = form.save(commit=False)
            # for review
            pesticide = Default_pesticide.objects.filter(
                pesticide_name=form.data['pesticide_name'])[0]
            try:
                total_review = pesticide.total_review + \
                    int(form.data['rating'])
                number_of_reviews = pesticide.number_of_reviews + 1
                avarage_review = round(total_review / number_of_reviews, 1)
                pesticide.total_review = total_review
                pesticide.number_of_reviews = number_of_reviews
                pesticide.avarage_review = avarage_review
                pesticide.save()
            except:
                pass
            planting = Planting.objects.filter(id=planting_id)[0]
            pesticide_date_from_planting = (datetime.fromisoformat(
                form.data['pesticide_date']).date() - planting.planting_time.date()).days
            form_save.pesticide_date_from_planting = pesticide_date_from_planting
            form_save.save()
            return redirect('pesticide_dose_info', dose_id=dose_id)
    data = {
        'pesticide_selection': pesticide_selection,
        'farmer_id': farmer_id,
        'farm_id': farm_id,
        'planting_id': planting_id,
        'dose_id': dose_id
    }
    return render(request, 'forms/pesticide_reg.html', data)


def search(request):
    farm_info = Farm_info.objects.values()
    farm = []
    s = []
    for i in farm_info:
        if farm:
            for j in farm:
                if i['farmer_id_id'] == j['farmer_id_id']:
                    j['farm_space'] += i['farm_space']
                    s = []
                    break
                else:
                    s.append(i)
            if s:
                farm.append(s[0])
                s = []
        else:
            farm.append(i)
    # farm = []
    # for i in farm_info:
    #     print("\n\n1", i)
    #     if farm:
    #         print("\n\nfarm", farm)
    #         for j in farm:
    #             print("\n\n", j)
    #             if j['farmer_id_id'] == i['farmer_id_id']:
    #                 print(i['farmer_id_id'], j['farmer_id_id'])
    #                 j['farm_space'] += i['farm_space']
    #             else:
    #                 farm.append(i)
    #     else:
    #         farm.append(i)
    # print("\n\n\n\n", farm)
    data = {'farm_info': farm}
    return render(request, 'forms/search.html', data)


def search_utm(request):
    farms = Farm_info.objects.all()
    farmers = Farmer.objects.all()
    temp_list = []
    for i in farms:
        temp_list.append([i.farmer_id.id, i.farm_space])
    temp_farmer_ids = []
    for i in range(len(temp_list)):
        temp_farmer_ids.append(temp_list[i][0])
    temp_farmer_ids = list(set(temp_farmer_ids))
    final_list = []
    f_list = []
    for i in farmers:
        for j in temp_farmer_ids:
            if i.id == j:
                f_list.append([j, i.name])
    for j, k in f_list:
        space = 0
        for i in range(len(temp_list)):
            if temp_list[i][0] == j:
                space += temp_list[i][1]
        final_list.append([j, space, k])
    data = {
        'final_list': final_list,
        'farmers': farmers,
    }
    return render(request, 'forms/search_utm.html', data)


@permission_required('is_staff', '403')
def default_parameters(request):
    return render(request, 'Default_parameters/default_parameters.html')


@permission_required('is_staff', '403')
def default_plant_name(request):
    seed_name = Default_plant_seed_name.objects.all()
    default_plant_name = list(Default_plant_name.objects.values())
    default_plant_seed_name = list(Default_plant_seed_name.objects.values())
    data = {
        'seed_name': seed_name,
        'default_plant_name': default_plant_name,
        'default_plant_seed_name': default_plant_seed_name
    }
    return render(request, 'Default_parameters/default_plant_name.html', data)


@permission_required('is_staff', '403')
def default_plant_name_reg(request):
    plant_names = Default_plant_name.objects.all()
    data = {
        'plant_names': plant_names
    }
    return render(request, 'Default_parameters/default_plant_name_reg.html', data)


@permission_required('is_staff', '403')
def add_default_plant_name(request):
    if request.method == 'POST':
        form = Default_plant_name_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('default_plant_name')


@permission_required('is_staff', '403')
def add_default_plant_seed_name(request):
    if request.method == 'POST':
        form = Default_plant_seed_name_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('default_plant_name')


@permission_required('is_staff', '403')
def add_default_fertilizer(request):
    if request.method == 'POST':
        form = Default_fertilizer_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_default_fertilizer')
    return render(request, 'Default_parameters/default_fertilizer_add.html')


@permission_required('is_staff', '403')
def default_fertilizers(request):
    default_fertilizer = Default_fertilizer.objects.all()
    data = {
        'default_fertilizer': default_fertilizer
    }
    return render(request, 'Default_parameters/default_fertilizer.html', data)


@permission_required('is_staff', '403')
def add_default_pesticide(request):
    if request.method == 'POST':
        form = Default_pesticide_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_default_pesticide')
    return render(request, 'Default_parameters/default_pesticide_add.html')


@permission_required('is_staff', '403')
def default_pesticides(request):
    default_pesticide = Default_pesticide.objects.all()
    data = {
        'default_pesticide': default_pesticide
    }
    return render(request, 'Default_parameters/default_pesticide.html', data)


def farmer_edit(request, farmer_id):
    if staff_permission(farmer_id, staff_type=request.user.is_staff):
        pass
    else:
        return redirect('403')
    farmer = Farmer.objects.get(id=farmer_id)
    farmers = Farmer.objects.filter(id=farmer_id)
    if request.method == 'POST':
        form = Farmer_Form(request.POST, instance=farmer)

        if form.is_valid():
            form.save()
            return redirect(f'/farmer_details/farmer_id={farmer_id}')

    return render(request, 'form_edit/farmer_edit.html', {'farmer': farmers})


def farm_edit(request, farm_id):
    farm = Farm_info.objects.get(id=farm_id)
    farms = Farm_info.objects.filter(id=farm_id)

    if request.method == 'POST':
        form = Farm_info_Form(request.POST, instance=farm)

        if form.is_valid():
            form.save()
            return redirect(f'/farm_info/farm_id={farm_id}')

    return render(request, 'form_edit/farm_edit.html', {'farms': farms})


def plant_edit(request, plant_id):
    plants = Planting.objects.filter(id=plant_id)
    plant = Planting.objects.get(id=plant_id)

    if request.method == 'POST':
        form = Planting_Form(request.POST, instance=plant)

        if form.is_valid():
            form.save()
            return redirect(f'/planting/planting_id={plant_id}')
    default_plant_name = list(Default_plant_name.objects.values())
    default_plant_seed_name_1 = Default_plant_seed_name.objects.all()
    default_plant_seed_name = []
    for plant_seed_name in default_plant_seed_name_1:
        default_plant_seed_name_dict = {}
        default_plant_seed_name_dict['plant_name'] = plant_seed_name.plant_name.plant_name
        default_plant_seed_name_dict['plant'] = plant_seed_name.seed_name
        default_plant_seed_name.append(default_plant_seed_name_dict)
    data = {
        'default_plant_name': default_plant_name,
        'default_plant_seed_name': default_plant_seed_name,
        'plants': plants}

    return render(request, 'form_edit/planting_edit.html', data)

def pesticide_dose_edit(request, pesticide_dose_id):
    Pesticides_dose = Pesticide_dose.objects.get(id=pesticide_dose_id)
    Pesticides_doses = Pesticide_dose.objects.filter(id=pesticide_dose_id)

    if request.method == 'POST':
        form = Pesticide_dose_Form(request.POST, instance=Pesticides_dose)

        if form.is_valid():
            form.save()
            return redirect(f'/pesticide_dose_info/pesticide_dose_id={pesticide_dose_id}')

    return render(request, 'form_edit/pesticide_dose_edit.html', {'Pesticides_dose': Pesticides_doses})

def fertilizer_edit(request, fertilizer_id):
    fertilizer = Fertilizer.objects.get(id=fertilizer_id)
    fertilizers = Fertilizer.objects.filter(id=fertilizer_id)

    if request.method == 'POST':
        form = Fertilizer_Form(request.POST, instance=fertilizer)

        if form.is_valid():
            form_save = form.save(commit=False)
            fertilizer_days_from_planting = (datetime.fromisoformat(
                form.data['fertilizer_date']).date() - fertilizer.planting_id.planting_time.date()).days
            form_save.fertilizer_days_from_planting = fertilizer_days_from_planting
            try:
                fertilizer = Default_fertilizer.objects.filter(
                    fertilizer_name=form.data['fertilizer_name'])[0]
                total_review = fertilizer.total_review + \
                    int(form.data['rating'])
                number_of_reviews = fertilizer.number_of_reviews + 1
                avarage_review = round(total_review / number_of_reviews, 1)
                fertilizer.total_review = total_review
                fertilizer.number_of_reviews = number_of_reviews
                fertilizer.avarage_review = avarage_review
                fertilizer.save()
            except:
                pass
            form_save.save()
            return redirect(f'/fertilizer_info/fertilizer_id={fertilizer_id}')

    return render(request, 'form_edit/fertilizer_edit.html', {'fertilizers': fertilizers})


def water_irrigation_edit(request, water_irrigation_id):
    water_irrigation = Water_irrigation.objects.get(id=water_irrigation_id)
    water_irrigations = Water_irrigation.objects.filter(id=water_irrigation_id)

    if request.method == 'POST':
        form = Water_irrigation_Form(request.POST, instance=water_irrigation)

        if form.is_valid():
            form_save = form.save(commit=False)
            water_date_from_planting = (datetime.fromisoformat(form.data['water_irrigation_date']).date(
            ) - water_irrigation.planting_id.planting_time.date()).days
            form_save.water_date_from_planting = water_date_from_planting
            form_save.save()
            return redirect(f'/water_irrigation_info/water_irrigation_id={water_irrigation_id}')

    return render(request, 'form_edit/water_irrigation_edit.html', {'water_irrigations': water_irrigations})


def pesticide_edit(request, pesticide_id):
    pesticide = Pesticide.objects.get(id=pesticide_id)
    pesticides = Pesticide.objects.filter(id=pesticide_id)
    if request.method == 'POST':
        form = Pesticide_Form(request.POST, instance=pesticide)

        if form.is_valid():
            form_save = form.save(commit=False)
            pesticide_date_from_planting = (datetime.fromisoformat(
                form.data['pesticide_date']).date() - pesticide.planting_id.planting_time.date()).days
            form_save.pesticide_date_from_planting = pesticide_date_from_planting
            try:
                pesticide = Default_pesticide.objects.filter(
                    pesticide_name=form.data['pesticide_name'])[0]
                total_review = pesticide.total_review + \
                    int(form.data['rating'])
                number_of_reviews = pesticide.number_of_reviews + 1
                avarage_review = round(total_review / number_of_reviews, 1)
                pesticide.total_review = total_review
                pesticide.number_of_reviews = number_of_reviews
                pesticide.avarage_review = avarage_review
                pesticide.save()
            except:
                pass
            form_save.save()
            return redirect(f'/pesticide_info/pesticide_id={pesticide_id}')

    return render(request, 'form_edit/pesticide_edit.html', {'pesticides': pesticides})


@permission_required('is_staff', '403')
def fertilizer_stats(request, fertilizer_name):
    fertilizer = Fertilizer.objects.filter(
        fertilizer_name=fertilizer_name).order_by('create_date')
    try:
        fertilizer_name = fertilizer[0].fertilizer_name
    except:
        fertilizer_name = 'No information about this fertilizer'
    data = {
        'fertilizer_name': fertilizer_name,
        'fertilizer': fertilizer
    }
    return render(request, 'stats/fertilizer_stats.html', data)


@permission_required('is_staff', '403')
def pesticide_stats(request, pesticide_name):
    pesticide = Pesticide.objects.filter(
        pesticide_name=pesticide_name).order_by('create_date')
    try:
        pesticide_name = pesticide[0].pesticide_name
    except:
        pesticide_name = 'No information about this pesticide'
    data = {
        'pesticide_name': pesticide_name,
        'pesticide': pesticide
    }
    return render(request, 'stats/pesticide_stats.html', data)
