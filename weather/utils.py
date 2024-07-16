import requests

weather_codes = {
    '0' : 'Чистое небо',
    '1, 2, 3' : 'Преимущественно ясно, переменная облачность, пасмурно',
    '45, 48' : 'Туман и отложения инейного тумана',
    '51, 53, 55' : 'Морось: легкая, умеренная и плотная',
    '56, 57' : 'Моросящий дождь: легкий и плотный',
    '61, 63, 65' : 'Дождь: слабый, умеренный и сильный',
    '66, 67' : 'Ледяной дождь: легкая и сильная интенсивность',
    '71, 73, 75' : 'Снегопад: слабый, умеренный и сильный',
    '77' : 'Снежных зерен',
    '80, 81, 82' : 'Ливни: слабые, умеренные и сильные',
    '85, 86' : 'Снежные ливни слабые и сильные',
    '95' : 'Гроза: легкая или умеренная',
    '96, 99' : 'Гроза с небольшим и сильным градом',
}

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    if 'current_weather' in data:
        return {
            'latitude': latitude,
            'longitude': longitude,
            'temperature': data['current_weather']['temperature'],
            'windspeed': data['current_weather']['windspeed'],
            'condition': weather_codes[code] if (code := str(data['current_weather']['weathercode'])) in weather_codes else data['current_weather']['weathercode']
        }
    return None


def get_coordinates(city_name):
    api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    response = requests.get(api_url)
    if response.status_code == 200 and response.json():
        try:
            data = response.json()['results'][0]
        except KeyError:
            message = f"Город {city_name} не найден"
            return None, None, message
        return float(data['latitude']), float(data['longitude']), None
    return None, None, None