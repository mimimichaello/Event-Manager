from django.urls import path

from .views import ListEventView, SendEventListView

urlpatterns = [
    path('', ListEventView.as_view(), name='list_event'),
    path('send/', SendEventListView.as_view(), name='send_event_list'),
]
