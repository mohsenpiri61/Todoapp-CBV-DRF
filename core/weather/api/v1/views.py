from rest_framework import viewsets
from weather.models import Weather
from .serializers import WeatherSerializer
from django.http import JsonResponse
#import requests



class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    
    # def __init__(self, latitude, longitude):
    #     self.lat= 36.0248825
    #     self.lang= 50.7574084
        
    def fetch_weather_data(self, latitude, longitude):
        base_url = "https://api.open-meteo.com/v1/forecast"
        params = {"latitude": self.lat, "longitude": self.long, "current_weather":true}  
        result = requests.get(base_url)
        return result.json()


    def save_weather_data(city):
        data = fetch_weather_data(36, 50)
        weather = Weather(
            
            temperature=data['current_weather']['temprature'],
            timestamp=data['current_weather']['time']
        )
        weather.save()
