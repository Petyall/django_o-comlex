# Weather Forecast Web Application

## Описание

Это веб-приложение позволяет пользователям вводить название города и получать прогноз погоды в этом городе на ближайшее время. Прогноз отображается в удобном и читаемом формате. Приложение использует [Django](https://www.djangoproject.com/) и [Django REST Framework](https://www.django-rest-framework.org/), а для получения данных о погоде и координатах города - API от [Open Meteo](https://open-meteo.com/).

### Основные функции

- Прогноз погоды для введенного города
- Автозаполнение (подсказки) при вводе города
- История поиска для каждого пользователя
- API, показывающее сколько раз вводили каждый город
- Скрипт, импортирующий города в базу данных из JSON файла

## Использованные технологии

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)

## Установка и запуск

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/Petyall/django_o-complex.git
cd django_o-complex
```

### Шаг 2: Создание и активация виртуального окружения 
```bash
python3 -m venv venv
source venv/bin/activate
```

### Шаг 3: Установка необходимых зависимостей 
```bash
pip3 install -r requirements.txt
```

### Шаг 4: Инициализация базы данных 
```bash
python3 manage.py migrate
```

### Шаг 5: Импортирование городов для автозаполнения при поиске 
```bash
python3 manage.py import_cities russian_cities.json 
```

### Шаг 6: Запуск локального сервера 
```bash
python3 manage.py runserver
```

## Тестирование
Для проверки работы Open Meteo API проект был покрыт юнит-тестами. Для их запуска используйте команду:
```bash
python3 weather/tests.py
```

## Примеры использования
- Перейдите на главную страницу, введите название города и нажмите "Получить погоду"
- Автодополнение поможет вам найти город
- История поиска будет отображаться ниже формы ввода
- Посетите API по адресу http://localhost:8000/api/city-search/ для просмотра статистики поиска городов