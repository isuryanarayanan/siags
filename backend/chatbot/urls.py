from simple_chatbot.views import SimpleChatbot
from django.urls import path, include

urlpatterns = [
    path("simple_chatbot/", SimpleChatbot.as_view())
]
