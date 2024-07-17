from django.shortcuts import render

from weather.open_meteo_api import get_weather, get_coordinates


def main(request):
    weather_info = None
    if 'city' in request.GET:
        city_name = request.GET['city']
        latitude, longitude, error_message = get_coordinates(city_name)
        if error_message:
            context = {'error_message': error_message}
            return render(request, 'weather/main.html', context)
        if latitude and longitude:
            weather_info = get_weather(latitude, longitude)
            weather_info['city'] = city_name
    context = {'weather_info': weather_info}
    return render(request, 'weather/main.html', context)
