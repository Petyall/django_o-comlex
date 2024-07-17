from django.shortcuts import render
from weather.open_meteo_api import get_weather, get_coordinates
from weather.models import City


def update_search_history(search_history: dict, city_name: str, max_length: int = 5) -> dict:
    """
    Обновляет историю поиска. Если city_name уже в истории, не добавляет его.
    Если длина истории превышает max_length, удаляет самый старый элемент.
    """
    if city_name in search_history:
        return search_history

    if len(search_history) >= max_length:
        search_history.pop(0)
    search_history.append(city_name)
    return search_history


def main(request):
    search_history = request.session.get('search_history', [])
    cities = City.objects.all()
    weather_info = None

    if 'city' in request.GET:
        city_name = request.GET['city']
        latitude, longitude, error_message = get_coordinates(city_name)
        
        if error_message:
            context = {
                'error_message': error_message,
                'cities': cities,
                'search_history': search_history
            }
            return render(request, 'weather/main.html', context)
        
        if latitude and longitude:
            weather_info = get_weather(latitude, longitude)
            weather_info['city'] = city_name
            search_history = update_search_history(search_history, city_name)
            request.session['search_history'] = search_history

            city_search, created = City.objects.get_or_create(name=city_name)
            city_search.number_of_searches += 1
            city_search.save()

    context = {
        'weather_info': weather_info,
        'cities': cities,
        'search_history': search_history
    }
    return render(request, 'weather/main.html', context)