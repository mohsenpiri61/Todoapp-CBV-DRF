from .views import AuthViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
    

app_name = "users"

router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")


urlpatterns = [
    path('token/login/', ObtainAuthToken.as_view(), name='token-login'),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name="jwt-refresh"),
    path('jwt/verify/', TokenVerifyView.as_view(), name="jwt-verify"),
]

urlpatterns += router.urls