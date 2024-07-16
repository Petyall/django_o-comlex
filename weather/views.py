from django.shortcuts import render

from weather.utils import get_weather, get_coordinates


def main(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET['city']
        latitude, longitude, message = get_coordinates(city)
        if latitude and longitude:
            print(latitude, longitude)
            weather_data = get_weather(latitude, longitude)
            weather_data['city'] = city
        if message:
            message_data = {'message': message}
            return render(request, 'weather/main.html', {'weather_data': weather_data, 'message_data': message_data})
    return render(request, 'weather/main.html', {'weather_data': weather_data})