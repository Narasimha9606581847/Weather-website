from django.urls import path
from . import views

app_name = 'weatherapp'  

urlpatterns = [
    path('', views.index, name='home'),
    path('weather/', views.index, name='weather'),
    path('delete/<str:city_name>/', views.delete_city, name='delete_city'),
]
