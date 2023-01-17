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
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Farm_info(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_nick_name = models.CharField(max_length=50, blank=True, null=True)
    farm_space = models.IntegerField(default=0)
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
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Soil_test(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    test_date = models.DateTimeField(blank=True,null=True)
    water_source = models.CharField(max_length=50, blank=True, null=True)
    ph = models.CharField(max_length=50, blank=True, null=True)
    ec = models.CharField(max_length=50, blank=True, null=True)
    organic_carbon = models.CharField(max_length=50, blank=True, null=True)
    available_nitrogen = models.CharField(max_length=50, blank=True, null=True)
    available_phosphorus = models.CharField(max_length=50, blank=True, null=True)
    available_potassium = models.CharField(max_length=50, blank=True, null=True)
    available_zinc = models.CharField(max_length=50, blank=True, null=True)
    available_boron = models.CharField(max_length=50, blank=True, null=True)
    available_iron = models.CharField(max_length=50, blank=True, null=True)
    available_manganese = models.CharField(max_length=50, blank=True, null=True)
    available_copper = models.CharField(max_length=50, blank=True, null=True)
    available_sulphur = models.CharField(max_length=50, blank=True, null=True)


class Water_test(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    test_date = models.DateTimeField(blank=True,null=True)
    sample_no = models.CharField(max_length=50, blank=True, null=True)
    ph = models.CharField(max_length=50, blank=True, null=True)
    ec = models.CharField(max_length=50, blank=True, null=True)
    tds = models.CharField(max_length=50, blank=True, null=True)
    ca = models.CharField(max_length=50, blank=True, null=True)
    mg = models.CharField(max_length=50, blank=True, null=True)
    hardness = models.CharField(max_length=50, blank=True, null=True)
    turbidity = models.CharField(max_length=50, blank=True, null=True)
    chloride = models.CharField(max_length=50, blank=True, null=True)


class Planting(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    planting_time = models.DateTimeField(max_length=50, blank=True, null=True)
    plant = models.CharField(max_length=50,blank=True, null=True)
    plant_type = models.CharField(max_length=50,blank=True, null=True)
    planting_area = models.CharField(max_length=50,blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)


class Harvesting(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    planting_id = models.ForeignKey(Planting, on_delete=models.CASCADE)
    plant_type = models.CharField(max_length=50)
    harvesting_time = models.DateTimeField(max_length=50,blank=True, null=True)
    total_production = models.IntegerField(blank=True, null=True)
    per_acre_production = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)


class Crop_selling(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    planting_id = models.ForeignKey(Planting, on_delete=models.CASCADE)
    sell_quantity = models.IntegerField(blank=True, null=True)
    sell_date = models.DateTimeField(blank=True, null=True)#selection
    sell_rate = models.IntegerField(blank=True, null=True)
    purchaser_name = models.CharField(max_length=50,blank=True, null=True)
    purchaser_number = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)


class Fertilizer(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    planting_id = models.ForeignKey(Planting, on_delete=models.CASCADE)
    fertilizer_name = models.CharField(max_length=50)
    fertilizer_qty_per_acre = models.CharField(max_length=50,blank=True, null=True)
    fertilizer_date = models.DateTimeField(blank=True, null=True)
    fertilizer_days_from_planting = models.IntegerField(default=0,blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)


class Water_irrigation(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    planting_id = models.ForeignKey(Planting, on_delete=models.CASCADE)
    water_irrigation_type = models.CharField(max_length=50, blank=True, null=True)
    water_irrigation_date = models.DateTimeField(blank=True, null=True)#selection
    water_date_from_planting = models.IntegerField(default=0,blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)

class Pesticide_dose(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    planting_id = models.ForeignKey(Planting, on_delete=models.CASCADE)
    dose_name = models.CharField(max_length=50)
    reason = models.CharField(max_length=150,blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)


class Pesticide(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    farm_id = models.ForeignKey(Farm_info, on_delete=models.CASCADE)
    planting_id = models.ForeignKey(Planting, on_delete=models.CASCADE)
    pesticide_name = models.CharField(max_length=50)
    dose_id = models.ForeignKey(Pesticide_dose, on_delete=models.CASCADE)
    purchased_from = models.BooleanField(default=True)
    pesticide_qty_per_acer = models.CharField(max_length=50,blank=True, null=True)
    reason = models.CharField(max_length=50,blank=True, null=True)
    pesticide_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)#selection
    pesticide_date_from_planting = models.IntegerField(default=0, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)

class Default_plant_name(models.Model):
    plant_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.plant_name

class Default_plant_seed_name(models.Model):
    plant_name = models.ForeignKey(Default_plant_name,on_delete=models.CASCADE)
    seed_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.seed_name

class Default_fertilizer(models.Model):
    fertilizer_name = models.CharField(max_length=50, unique=True)
    total_review = models.IntegerField(default=0)
    number_of_reviews = models.IntegerField(default=0)
    avarage_review = models.FloatField(default=0.0)
    def __str__(self):
        return self.fertilizer_name

class Default_pesticide(models.Model):
    pesticide_name = models.CharField(max_length=50, unique=True)
    total_review = models.IntegerField(default=0)
    number_of_reviews = models.IntegerField(default=0)
    avarage_review = models.FloatField(default=0.0)
    def __str__(self):
        return self.pesticide_name