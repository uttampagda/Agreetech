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
    path('farmer_details/<int:Id>', views.view_farmer, name="farmer_details"),
    # path('Farmer', views.Farmer, name="Farmer"),
    path('farmers', views.farmers, name="farmers"),
    path('Soil_test', views.soil_test, name="Soil_test"),
    path('Farm_info/<int:farmer_id>', views.farm_info, name="Farm_info"),
    path('Planting', views.planting, name="Planting"),
    path('Harvesting', views.harvesting, name="Harvesting"),
    path('Crop_selling', views.crop_selling, name="Crop_selling"),
    path('Fertilizer', views.fertilizer, name="Fertilizer"),
    path('Water_irrigation', views.water_irrigation, name="Water_irrigation"),
    path('Pesticide', views.pesticide, name="Pesticide"),
]
