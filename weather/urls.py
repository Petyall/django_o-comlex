from django.urls import path
from weather.views import main

app_name = 'weather'

urlpatterns = [
    path('', main, name='main'),
]
