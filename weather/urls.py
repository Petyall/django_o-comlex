from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weather.views import main
from weather.api_views import CitySearchViewSet

app_name = 'weather'

router = DefaultRouter()
router.register(r'city_search', CitySearchViewSet, basename='city_search')

urlpatterns = [
    path('', main, name='main'),
    path('api/', include(router.urls)),
]