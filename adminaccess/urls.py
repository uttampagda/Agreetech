from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('403', views.permission_denied, name="403"),
    path('logout', views.logout, name="logout"),
    path('createuser', views.createuser, name="createuser"),
    path('', views.dashboard, name="dashboard"),
    path('forms', views.forms, name="forms"),
    path('farmer_registration', views.farmer_registration, name="farmer_registration"),
    path('farmer_details/farmer_id=<int:farmer_id>', views.farmer_details, name="farmer_details"),
    # path('Farmer', views.Farmer, name="Farmer"),
    path('farmers', views.farmers, name="farmers"),
    path('soil_test', views.soil_test, name="soil_test"),
    path('farm_info_reg', views.farm_info_reg, name="farm_info_reg"),
    path('farm_info/farm_id=<int:farm_id>', views.farm_info, name="farm_info"),
    path('planting_reg', views.planting_reg, name="planting_reg"),
    path('planting/planting_id=<int:planting_id>', views.planting, name="planting"),
    # path('planting/<int:farmer_id>', views.planting, name="planting"),
    path('harvesting_and_crop_selling', views.harvesting_and_crop_selling, name="harvesting_and_crop_selling"),
    path('harvesting_reg', views.harvesting_reg, name="harvesting_reg"),
    path('crop_selling_reg', views.crop_selling_reg, name="crop_selling_reg"),
    path('fertilizer_reg', views.fertilizer_reg, name="fertilizer_reg"),
    path('fertilizer_info/fertilizer_id=<int:fertilizer_id>', views.fertilizer_info, name="fertilizer_info"),
    path('Water_irrigation_reg', views.water_irrigation_reg, name="water_irrigation_reg"),
    path('water_irrigation_info/water_irrigation_id=<int:water_irrigation_id>', views.water_irrigation_info, name="water_irrigation_info"),
    path('Pesticide_reg', views.pesticide_reg, name="pesticide_reg"),
    path('pesticide_info/pesticide_id=<int:pesticide_id>', views.pesticide_info, name="pesticide_info"),
    path('search', views.search, name="search"),
    path('search_utm', views.search_utm, name="search_utm"),
    path('default_parameters', views.default_parameters, name="default_parameters"),
    path('default_plant_name', views.default_plant_name, name="default_plant_name"),
    path('add_default_plant_name', views.add_default_plant_name, name="add_default_plant_name"),
    path('select_default_plant_name', views.select_default_plant_name, name="select_default_plant_name"),
    path('farmer_edit/farmer_id=<int:farmer_id>', views.farmer_edit, name="farmer_edit"),
    path('farm_edit/farm_id=<int:farm_id>', views.farm_edit, name="farm_edit"),
    path('plant_edit/plant_id=<int:plant_id>', views.plant_edit, name="plant_edit"),
    path('fertilizer_edit/fertilizer_id=<int:fertilizer_id>', views.fertilizer_edit, name="fertilizer_edit"),
    path('water_irrigation_edit/water_irrigation_id=<int:water_irrigation_id>', views.water_irrigation_edit, name="water_irrigation_id_edit"),
    path('pesticide_edit/pesticide_id=<int:pesticide_id>', views.pesticide_edit, name="Pesticide_edit"),


    

    

]
