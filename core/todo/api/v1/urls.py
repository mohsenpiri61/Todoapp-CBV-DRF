from rest_framework.routers import DefaultRouter
from .views import TodoListView, TodoDetailApiView


app_name = "api-v1"


router = DefaultRouter()
router.register("task-list", TodoListView, basename="task")
# router.register("task-detail",TodoDetailApiView, basename="task_detail")


urlpatterns = router.urls