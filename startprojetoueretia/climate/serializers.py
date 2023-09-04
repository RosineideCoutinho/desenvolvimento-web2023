from rest_framework import serializers
from .models import Forecast


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['name', 'city', 'country', 'temperature', 'description', 'humidity', 'wind']

