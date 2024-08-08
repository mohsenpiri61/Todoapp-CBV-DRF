from rest_framework.response import Response
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# import time 
from django.http import JsonResponse
import requests


# @method_decorator(cache_page(60 * 60 * 2), 'dispatch')
class TodoListView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def list(self, request):
        # Note the use of 'get_queryset()' instead of 'self.queryset'
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        # time.sleep(5)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailApiView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "todo_id"

    def get_object(self, queryset=None):
        obj = Task.objects.get(pk=self.kwargs["todo_id"])
        return obj

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return Response({"detail": "successfully removed"})

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = TaskSerializer(
            data=request.data, instance=object, many=False
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class GetWeatherAPI():
    
    def __init__(self, latitude, longitude):
        self.lat= 36.0248825
        self.lang= 50.7574084
        
    def get_current_weather(self):
        base_url = "https://api.open-meteo.com/v1/forecast"
        params = {"latitude": self.lat, "longitude": self.long, "current_weather":true}  
        result = requests.get(base_url)
        return JsonResponse(result.json())  