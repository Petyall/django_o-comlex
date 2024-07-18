from django.urls import include, path
from rest_framework.routers import DefaultRouter

from weather.api_views import CitySearchViewSet
from weather.views import main

app_name = 'weather'

router = DefaultRouter()
router.register(r'city_search', CitySearchViewSet, basename='city_search')

urlpatterns = [
    path('', main, name='main'),
    path('api/', include(router.urls)),
]
