from rest_framework.routers import DefaultRouter
from .views import TodoListView, GetWeatherAPI


app_name = "api-v1"


router = DefaultRouter()
router.register("task-list", TodoListView, basename="task")
router.register("open-meteo", GetWeatherAPI, basename="meteo")



urlpatterns = router.urls