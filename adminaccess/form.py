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
        fields = ['farmer_id', 'farm_id', 'test_year', 'soil_test', 'water_test', 'nitrogen', 'phosphorus', 'potassium',
                  'other_element', 'test_file']


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
                  'purchaser_number']


class Fertilizer_Form(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['farmer_id', 'farm_id', 'planting_id', 'fertilizer_name', 'fertilizer_qty', 'fertilizer_qty_per_acre',
                  'rating', 'crop_days']


class Water_irrigation_Form(forms.ModelForm):
    class Meta:
        model = Water_irrigation
        fields = ['farmer_id', 'farm_id', 'planting_id', 'water_irrigation_type', 'crop_days']


class Pesticide_Form(forms.ModelForm):
    class Meta:
        model = Pesticide
        fields = ['farmer_id', 'farm_id', 'planting_id', 'pesticide_name', 'pesticide_qty', 'reason', 'pesticide_days']