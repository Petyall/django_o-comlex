import unittest
from unittest.mock import patch, MagicMock
from open_meteo_api import get_weather_condition, get_weather, get_coordinates

class TestOpenMeteoAPI(unittest.TestCase):

    @patch('open_meteo_api.requests.get')
    def test_get_weather_condition(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": [{"latitude": 45.0, "longitude": 45.0}]}
        mock_get.return_value = mock_response

        condition = get_weather_condition(0)
        self.assertEqual(condition, "Чистое небо")

    @patch('open_meteo_api.requests.get')
    def test_get_weather(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"current_weather": {"temperature": 25, "windspeed": 5, "weathercode": 0}}
        mock_get.return_value = mock_response

        weather_info = get_weather(45.0, 45.0)
        self.assertEqual(weather_info['temperature'], 25)
        self.assertEqual(weather_info['windspeed'], 5)
        self.assertEqual(weather_info['condition'], "Чистое небо")

    @patch('open_meteo_api.requests.get')
    def test_get_coordinates(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"results": [{"latitude": 45.0, "longitude": 45.0}]}

        mock_get.return_value = mock_response

        latitude, longitude, error_message = get_coordinates('Moscow')
        self.assertEqual(latitude, 45.0)
        self.assertEqual(longitude, 45.0)
        self.assertIsNone(error_message)

if __name__ == '__main__':
    unittest.main()

