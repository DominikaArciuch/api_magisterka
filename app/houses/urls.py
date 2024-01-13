from django.urls import path

from .views import HouseListCreateView, HouseDetailView

urlpatterns = [
    path("", HouseListCreateView.as_view()),
    path("<str:pk>/", HouseDetailView.as_view()),
]