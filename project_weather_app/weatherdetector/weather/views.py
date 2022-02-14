from django.shortcuts import render
import json 
import urllib.request
import logging

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=eb6ccf6e81e349ab752f3d414315c607').read()
        json_data = json.loads(res)
        data = {
            "city": str(json_data['name']),
            "country_code": str(json_data['sys']['country']),
            "coordinates": str(json_data['coord']['lon']) + "," + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "temp_min": str(json_data['main']['temp_min']),
            "temp_max": str(json_data['main']['temp_max']),
            "wind_speed": str(json_data['wind']['speed']),
            "wind_deg": str(json_data['wind']['deg']),
            "clouds": str(json_data['clouds']['all']),
            "weather_description": str(json_data['weather'][0]['description']),
            # "weather_icon": str(json_data['weather'][0]['icon']),
            "weather_main": str(json_data['weather'][0]['main']),
        }
    else:
        data = {}
    print(data)
    return render(request, 'index.html', data)
    