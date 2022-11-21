from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Farmer)
admin.site.register(Farm_info)
admin.site.register(Soil_test)
admin.site.register(Planting)
admin.site.register(Harvesting)
admin.site.register(Crop_selling)
admin.site.register(Fertilizer)
admin.site.register(Water_irrigation)
admin.site.register(Pesticide)
admin.site.register(Pesticide_dose)
admin.site.register(Default_plant_name)
admin.site.register(Default_plant_seed_name)
admin.site.register(Default_fertilizer)
admin.site.register(Default_pesticide)
