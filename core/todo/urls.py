from django.urls import path, include
from .views import (
    Home,
    TaskList, 
    TaskDetail, 
    TaskCreate, 
    TaskUpdate,
    TaskDelete
)

app_name = 'todo'

urlpatterns = [
    path('', Home, name='home'),
    path('list/', TaskList.as_view(), name="task-list"),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path("api/v1/", include("todo.api.v1.urls")),
]
