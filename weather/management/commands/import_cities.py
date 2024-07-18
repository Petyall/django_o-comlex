import json

from django.core.management.base import BaseCommand

from weather.models import City


class Command(BaseCommand):
    """
    Команда для загрузки городов из JSON-файла
    """
    help = 'Загрузка городов из JSON-файла'

    # Добавление аргументов командной строки
    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='JSON-файл с городами')

    # Обработка действия команды
    def handle(self, *args, **kwargs):
        # Получение пути к JSON-файлу
        json_file = kwargs['json_file']
        with open(json_file, 'r', encoding='utf-8') as file:
            # Чтение содержимого JSON-файла
            data = json.load(file)
            # Добавление городов в базу данных из JSON-файла
            for item in data:
                city, created = City.objects.get_or_create(
                    name=item['name'],
                    defaults={'region': item.get('region')}
                )
                # Вывод сообщения о добавлении города
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Успешно добавлен город: {city.name}'))
                # Вывод сообщения о том, что город уже существует
                else:
                    self.stdout.write(self.style.WARNING(f'Город уже существует: {city.name}'))
