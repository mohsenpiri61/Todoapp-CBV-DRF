from .views import AuthViewSet
from rest_framework.routers import DefaultRouter

app_name = "users"

router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")

urlpatterns = router.urls