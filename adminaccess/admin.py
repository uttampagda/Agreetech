from django.contrib import admin
from .models import Farmer, Farm_info, Soil_test, Planting

# Register your models here.

admin.site.register(Farmer)
admin.site.register(Farm_info)
admin.site.register(Soil_test)
admin.site.register(Planting)


