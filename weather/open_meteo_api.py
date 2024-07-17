import requests

from typing import Optional, Dict, Tuple


# Коды погоды Open Meteo API
weather_codes = {
    (0,): 'Чистое небо',
    (1, 2, 3): 'Преимущественно ясно, переменная облачность, пасмурно',
    (45, 48): 'Туман и отложения инейного тумана',
    (51, 53, 55): 'Морось: легкая, умеренная и плотная',
    (56, 57): 'Моросящий дождь: легкий и плотный',
    (61, 63, 65): 'Дождь: слабый, умеренный и сильный',
    (66, 67): 'Ледяной дождь: легкая и сильная интенсивность',
    (71, 73, 75): 'Снегопад: слабый, умеренный и сильный',
    (77,): 'Снежных зерен',
    (80, 81, 82): 'Ливни: слабые, умеренные и сильные',
    (85, 86): 'Снежные ливни слабые и сильные',
    (95,): 'Гроза: легкая или умеренная',
    (96, 99): 'Гроза с небольшим и сильным градом',
}


def get_weather_condition(code: int) -> str:
    """
    Возвращает текстовое описание погоды по коду, предоставленному Open Meteo API
    """
    for codes, condition in weather_codes.items():
        if code in codes:
            return condition
    return f"Неизвестный код: {code}"


def get_weather(latitude: float, longitude: float) -> Optional[Dict[str, str]]:
    """
    Возвращает словарь с данными о погоде по координатам, предоставленным Open Meteo API
    """
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(api_url)
    response_data = response.json()
    if 'current_weather' in response_data:
        return {
            'temperature': response_data['current_weather']['temperature'],
            'windspeed': response_data['current_weather']['windspeed'],
            'condition': get_weather_condition(response_data['current_weather']['weathercode'])
        }
    return None


def get_coordinates(city_name: str) -> Tuple[Optional[float], Optional[float], Optional[str]]:
    """
    Запрашивает координаты города по его названию с помощью Open Meteo API
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    response = requests.get(url)

    if response.status_code == 200 and response.json():
        try:
            response_data = response.json()["results"][0]
        except KeyError:
            return None, None, f"Город {city_name} не найден"

        return (
            float(response_data["latitude"]),
            float(response_data["longitude"]),
            None,
        )

    return None, None, None

# https://open-meteo.com/en/docs/geocoding-api
# https://open-meteo.com/en/docs#location_mode=csv_coordinates
