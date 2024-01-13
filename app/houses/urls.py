from django.urls import path

from .views import HouseListCreateView, HouseDetailView

urlpatterns = [
    path("", HouseListCreateView.as_view()),
    path("<int:pk>/", HouseDetailView.as_view()),
]