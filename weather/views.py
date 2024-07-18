from django.shortcuts import render

from weather.models import City
from weather.open_meteo_api import get_coordinates, get_weather


def update_search_history(search_history: dict, city_name: str, max_length: int = 5) -> dict:
    """
    Обновляет историю поиска. Если city_name уже в истории, не добавляет его.
    Если длина истории превышает max_length, удаляет самый старый элемент.
    """

    # Если город уже в истории поиска, он не добавляется
    if city_name in search_history:
        return search_history

    # Если длина истории поиска превышает max_length, удаляется самый старый элемент
    if len(search_history) >= max_length:
        search_history.pop(0)
            
    # Добавление города в историю поиска
    search_history.append(city_name)
    return search_history


def main(request):
    # Получение истории поиска из сессии
    search_history = request.session.get('search_history', [])
    # Получение списка городов из базы данных
    cities = City.objects.all()
    # Инициализация переменной для работы с информацией о погоде
    weather_info = None

    if 'city' in request.GET:
        # Получение города из GET-запроса
        city_name = request.GET['city']
        # Попытка получения координат города
        latitude, longitude, error_message = get_coordinates(city_name)
        
        # Обработка ошибки когда город не найден
        if error_message:
            context = {
                'error_message': error_message,
                'cities': cities,
                'search_history': search_history
            }
            return render(request, 'weather/main.html', context)
        
        # Если город и координаты получены, получаем информацию о погоде
        if latitude and longitude:
            # Получение информации о погоде
            weather_info = get_weather(latitude, longitude)
            weather_info['city'] = city_name
            # Обновление истории поиска
            search_history = update_search_history(search_history, city_name)
            request.session['search_history'] = search_history

            # Обновление счетчика поиска городов
            city_search, created = City.objects.get_or_create(name=city_name)
            city_search.number_of_searches += 1
            city_search.save()

    # Передача полученных данных в HTML
    context = {
        'weather_info': weather_info,
        'cities': cities,
        'search_history': search_history
    }
    return render(request, 'weather/main.html', context)
