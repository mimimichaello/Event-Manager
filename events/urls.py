from django.urls import path

from .views import ListEventView

urlpatterns = [
    path('', ListEventView.as_view(), name='list_event'),
]
