from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet

router = DefaultRouter()
router.register("open-meteo", WeatherViewSet, basename="meteo")

urlpatterns = router.urls


