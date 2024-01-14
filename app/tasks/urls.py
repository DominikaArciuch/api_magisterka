from django.urls import path
from .views import CreateTaskView, TaskDetailView, BaseTasksView

urlpatterns = [
    path("", CreateTaskView.as_view()),
    path("<int:pk>/", TaskDetailView.as_view()),
    path("base/", BaseTasksView.as_view()),
]