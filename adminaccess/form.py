from django import forms
from django.db.models import fields
from .models import *


class Farmer_Form(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'phone_number', 'address', 'aadhar_number', 'family_members', 'family_occupation',
                  'is_access']


class Farm_info_Form(forms.ModelForm):
    class Meta:
        model = Farm_info
        fields = ['farmer_id', 'farm_nick_name', 'farm_space', 'geo_location', 'farm_village', 'khata_no',
                  'who_caretaker', 'caretaker', 'caretaker_phone_number', 'soil_type', 'water_source', 'water_type',
                  'water_season']


class Soil_test_Form(forms.ModelForm):
    class Meta:
        model = Soil_test
        fields = ['farmer_id', 'farm_id', 'test_date', 'water_source', 'ph', 'ec', 'organic_carbon', 'available_nitrogen',
                  'available_phosphorus', 'available_potassium','available_zinc','available_boron','available_iron',
                  'available_manganese','available_copper','available_sulphur']


class Water_test_Form(forms.ModelForm):
    class Meta:
        model = Water_test
        fields = ['farmer_id', 'farm_id', 'test_date', 'sample_no', 'ph', 'ec', 'tds', 'ca',
                  'mg', 'hardness','turbidity','chloride']


class Planting_Form(forms.ModelForm):
    class Meta:
        model = Planting
        fields = ['farmer_id', 'farm_id', 'planting_time', 'plant', 'plant_type', 'planting_area']


class Harvesting_Form(forms.ModelForm):
    class Meta:
        model = Harvesting
        fields = ['farmer_id', 'farm_id', 'planting_id', 'plant_type', 'harvesting_time', 'total_production',
                  'per_acre_production']


class Crop_selling_Form(forms.ModelForm):
    class Meta:
        model = Crop_selling
        fields = ['farmer_id', 'farm_id', 'planting_id', 'sell_quantity', 'sell_rate', 'purchaser_name',
                  'purchaser_number', 'sell_date']


class Fertilizer_Form(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['farmer_id', 'farm_id', 'planting_id', 'fertilizer_name', 'fertilizer_qty_per_acre',
                  'fertilizer_date', 'rating', 'fertilizer_days_from_planting']


class Water_irrigation_Form(forms.ModelForm):
    class Meta:
        model = Water_irrigation
        fields = ['farmer_id', 'farm_id', 'planting_id', 'water_irrigation_type', 'water_irrigation_date','water_date_from_planting']

class Pesticide_dose_Form(forms.ModelForm):
    class Meta:
        model = Pesticide_dose
        fields = ['farmer_id', 'farm_id', 'planting_id', 'dose_name', 'reason']


class Pesticide_Form(forms.ModelForm):
    class Meta:
        model = Pesticide
        fields = ['farmer_id', 'farm_id', 'planting_id','dose_id', 'pesticide_name','pesticide_qty_per_acer','purchased_from' ,'reason' ,'pesticide_date_from_planting', 'rating']

class Default_plant_name_Form(forms.ModelForm):
    class Meta:
        model = Default_plant_name
        fields = ['plant_name']

class Default_plant_seed_name_Form(forms.ModelForm):
    class Meta:
        model = Default_plant_seed_name
        fields = ['plant_name' , 'seed_name']

class Default_fertilizer_Form(forms.ModelForm):
    class Meta:
        model = Default_fertilizer
        fields = ['fertilizer_name']

class Default_pesticide_Form(forms.ModelForm):
    class Meta:
        model = Default_pesticide
        fields = ['pesticide_name']