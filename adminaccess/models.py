from django.db import models


# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.TextField()
    aadhar_number = models.IntegerField(blank=True, null=True)
    family_members = models.IntegerField(blank=True, null=True)
    family_occupation = models.CharField(max_length=50, blank=True, null=True)
    is_access = models.BooleanField(default=False)


class Farm_info(models.Model):
    farmer_id = models.IntegerField()
    farm_nick_name = models.CharField(max_length=50, blank=True, null=True)
    farm_space = models.IntegerField()
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    farm_village = models.CharField(max_length=50, blank=True, null=True)
    khata_no = models.CharField(max_length=50, blank=True, null=True)
    who_caretaker = models.CharField(max_length=50, blank=True, null=True)
    caretaker = models.CharField(max_length=50, blank=True, null=True)
    caretaker_phone_number = models.IntegerField(blank=True, null=True)
    soil_type = models.CharField(max_length=50, blank=True, null=True)
    water_source = models.CharField(max_length=50, blank=True, null=True)
    water_type = models.CharField(max_length=50, blank=True, null=True)
    water_season = models.CharField(max_length=50, blank=True, null=True)


class Soil_test(models.Model):
    farmer_id = models.IntegerField()
    farm_id = models.IntegerField()
    test_year = models.IntegerField()
    soil_test = models.CharField(max_length=50, blank=True, null=True)
    water_test = models.CharField(max_length=50, blank=True, null=True)
    nitrogen = models.CharField(max_length=50, blank=True, null=True)
    phosphorus = models.CharField(max_length=50, blank=True, null=True)
    potassium = models.CharField(max_length=50, blank=True, null=True)
    other_element = models.CharField(max_length=50, blank=True, null=True)
    test_file = models.FileField(upload_to=str(farm_id) + '/' + 'soil_test', blank=True, null=True)


class Planting(models.Model):
    farmer_id = models.IntegerField()
    farm_id = models.IntegerField()
    planting_time = models.CharField(max_length=50, blank=True, null=True)
    plant = models.CharField(max_length=50)
    plant_type = models.CharField(max_length=50)
    planting_area = models.CharField(max_length=50)


class Harvesting(models.Model):
    farmer_id = models.IntegerField()
    farm_id = models.IntegerField()
    planting_id = models.IntegerField()
    plant_type = models.CharField(max_length=50)
    harvesting_time = models.CharField(max_length=50)
    total_production = models.IntegerField()
    per_acre_production = models.IntegerField()
    sell_quantity = models.IntegerField()
    sell_date = models.CharField(max_length=50)
    sell_rate = models.IntegerField()
    purchaser_name = models.CharField(max_length=50)
    purchaser_number = models.IntegerField()


class Crop_selling(models.Model):
    farmer_id = models.IntegerField()
    farm_id = models.IntegerField()
    harvesting_id = models.IntegerField()
    sell_quantity = models.IntegerField()
    sell_date = models.CharField(max_length=50)
    sell_rate = models.IntegerField()
    purchaser_name = models.CharField(max_length=50)
    purchaser_number = models.IntegerField()


class Fertilizer(models.Model):
    farmer_id = models.IntegerField()
    farm_id = models.IntegerField()
    planting_id = models.IntegerField()
    fertilizer_name = models.CharField(max_length=50)
    fertilizer_qty = models.CharField(max_length=50)
    fertilizer_qty_per_acre = models.CharField(max_length=50)
    fertilizer_date = models.DateField()
    rating = models.IntegerField()
    crop_days = models.CharField(max_length=50)


class Water_irrigation(models.Model):
    farmer_id = models.IntegerField()
    farm_id = models.IntegerField()
    planting_id = models.IntegerField()
    water_irrigation_type = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    crop_days = models.CharField(max_length=50, blank=True, null=True)


class Pesticide(models.Model):
    farmer_id = models.IntegerField()
    farm_id = models.IntegerField()
    planting_id = models.IntegerField()
    pesticide_name = models.CharField(max_length=50)
    pesticide_qty = models.CharField(max_length=50)
    pesticide_date = models.DateField()
    pesticide_days = models.CharField(max_length=50, blank=True, null=True)