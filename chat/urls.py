from django.urls import path

from chat.views import (
    MessageListCreateAPIView, MessageDetailAPIView,
    GroupListCreateAPIView, GroupDetailAPIView
)


urlpatterns = [
    path("", MessageListCreateAPIView.as_view()),
    path("<int:pk>", MessageDetailAPIView.as_view()),
    path("groups/", GroupListCreateAPIView.as_view()),
    path("groups/<int:pk>", GroupDetailAPIView.as_view())
]