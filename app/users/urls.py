from django.urls import path

from . import views

urlpatterns = [
    path("filter/", views.UserFilterView.as_view()),
]
