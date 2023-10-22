from rest_framework import viewsets
from .serializers import ForecastSerializer
from .models import Forecast


class ForecastViewSet(viewsets.ModelViewSet):
    model = Forecast
    serializer_class = ForecastSerializer
    queryset = Forecast.objects.all()
    filter_fields = ('name', 'city', 'coutry', 'temperature', 'description', 'humidity', 'wid')
