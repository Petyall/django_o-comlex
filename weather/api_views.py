from rest_framework import viewsets

from weather.models import City
from weather.serializers import CitySearchSerializer


class CitySearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.filter(number_of_searches__gt=0)
    serializer_class = CitySearchSerializer
