from django.contrib import admin
from .models import Farmer, Farm_info, Soil_test, Planting, Harvesting, Crop_selling, Fertilizer, Water_irrigation, Pesticide

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
