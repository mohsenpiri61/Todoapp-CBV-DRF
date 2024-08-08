from rest_framework import viewsets
from weather.models import Weather
from .serializers import WeatherSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
