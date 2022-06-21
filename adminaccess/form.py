from django import forms
from django.db.models import fields
from .models import *

class Farmer_Form(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'phone_number', 'address', 'aadhar_number', 'family_members', 'family_occupation', 'is_access']
        
class Farm_info_Form(forms.ModelForm):
    class Meta:
        model = Farm_info
        fields = ['farmer_id', 'farm_nick_name', 'farm_space' ,'geo_location','farm_village', 'khata_no', 'who_caretaker', 'caretaker', 'caretaker_phone_number', 'soil_type' ,'water_source','water_type', 'water_season']
        
class Soil_test_Form(forms.ModelForm):
    class Meta:
        model = Soil_test
        fields = ['farmer_id', 'farm_id', 'test_year', 'soil_test', 'water_test', 'nitrogen', 'phosphorus', 'potassium', 'other_element', 'test_file']
 