from rest_framework import serializers

from weather.models import City


class CitySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'number_of_searches']
