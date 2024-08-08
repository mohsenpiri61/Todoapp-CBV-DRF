from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet

router = DefaultRouter()
router.register("open-meteo", GetWeatherAPI, basename="meteo")

urlpatterns = [
    path('', include(router.urls)),
]


