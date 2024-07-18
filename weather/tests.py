import unittest
from unittest.mock import MagicMock, patch

from open_meteo_api import get_coordinates, get_weather, get_weather_condition


class TestOpenMeteoAPI(unittest.TestCase):

    @patch('open_meteo_api.requests.get')
    def test_get_weather_condition(self, mock_get):
        # Создание mock-объект для ответа от API
        mock_response = MagicMock()
        # Определение, что метод json() у mock-ответа будет возвращать
        # пример JSON-ответа с координатами
        mock_response.json.return_value = {"results": [{"latitude": 45.0, "longitude": 45.0}]}
        # Определение, что метод get() будет возвращать mock-ответ
        mock_get.return_value = mock_response

        # Вызов функции для получения погодного условия и проверка результата
        condition = get_weather_condition(0)
        self.assertEqual(condition, "Чистое небо")

    @patch('open_meteo_api.requests.get')
    def test_get_weather(self, mock_get):
        # Создание mock-объект для ответа от API
        mock_response = MagicMock()
        # Определение, что метод json() у mock-ответа будет возвращать
        # пример JSON-ответа с текущей погодой
        mock_response.json.return_value = {"current_weather": {"temperature": 25, "windspeed": 5, "weathercode": 0}}
        # Определение, что метод get() будет возвращать mock-ответ
        mock_get.return_value = mock_response

        # Вызов функции для получения погоды и проверка результата
        weather_info = get_weather(45.0, 45.0)
        self.assertEqual(weather_info['temperature'], 25)
        self.assertEqual(weather_info['windspeed'], 5)
        self.assertEqual(weather_info['condition'], "Чистое небо")

    @patch('open_meteo_api.requests.get')
    def test_get_coordinates(self, mock_get):
        # Создание mock-объект для ответа от API
        mock_response = MagicMock()
        # Устанавка успешного статус кода
        mock_response.status_code = 200
        # Определение, что метод json() у mock-ответа будет возвращать
        # пример JSON-ответа с координатами
        mock_response.json.return_value = {"results": [{"latitude": 45.0, "longitude": 45.0}]}
        # Определение, что метод get() будет возвращать mock-ответ
        mock_get.return_value = mock_response

        # Вызов функции для получения координат и проверка результата
        latitude, longitude, error_message = get_coordinates('Moscow')
        self.assertEqual(latitude, 45.0)
        self.assertEqual(longitude, 45.0)
        self.assertIsNone(error_message)


if __name__ == '__main__':
    unittest.main()
