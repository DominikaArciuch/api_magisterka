from django.urls import path

from .views import SendInvitationView, InvitationView

urlpatterns = [
    path("", SendInvitationView.as_view()),
    path("<str:pk>/", InvitationView.as_view()),
]
