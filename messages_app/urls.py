from django.urls import path
from .views import MessageCreateView, MessageListView, message_list_view, clear_messages

urlpatterns = [
    path('messages/', MessageCreateView.as_view(), name='message-create'),
    path('messages/list/', MessageListView.as_view(), name='message-list'),
    path('messages/view/', message_list_view, name='message-list-view'),
    path('messages/clear/', clear_messages, name='message-clear'),
]
