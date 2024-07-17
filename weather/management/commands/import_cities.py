import json
from django.core.management.base import BaseCommand
from weather.models import City

class Command(BaseCommand):
    help = 'Загрузка городов из JSON-файла'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='JSON-файл с городами')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                city, created = City.objects.get_or_create(
                    name=item['name'],
                    defaults={'region': item.get('region')}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Успешно добавлен город: {city.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Город уже существует: {city.name}'))
