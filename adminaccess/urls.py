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
    path('planting', views.planting, name="planting"),
    # path('planting/<int:farmer_id>', views.planting, name="planting"),
    path('Harvesting', views.harvesting, name="Harvesting"),
    path('Crop_selling', views.crop_selling, name="Crop_selling"),
    path('Fertilizer', views.fertilizer, name="Fertilizer"),
    path('Water_irrigation', views.water_irrigation, name="Water_irrigation"),
    path('Pesticide', views.pesticide, name="Pesticide"),
]
