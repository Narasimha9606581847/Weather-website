from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import city as City
from .forms import cityForms

def index(request):
    cities = City.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST':
        form = cityForms(request.POST)
        if form.is_valid():
            form.save()

    form = cityForms()
    weather_data = []

    for c in cities:
        city_weather = requests.get(url.format(c.name)).json()

        if city_weather.get('main'):
            weather = {
                'city': c.name,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)


def delete_city(request, city_name):
    if request.method == "GET":
        cities = City.objects.filter(name=city_name)
        if cities.exists():
            cities.delete()
        return redirect('weatherapp:home')