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
    path('Farmer', views.Farmer, name="Farmer"),
    path('Soil_test', views.Soil_test, name="Soil_test"),
    path('Farm_info', views.Farm_info, name="Farm_info"),
    path('farmer_details', views.farmer_details, name="farmer_details"),
    path('farm_info', views.farm_info, name="farm_info"),
    path('soil_test', views.soil_test, name="soil_test"),


]
