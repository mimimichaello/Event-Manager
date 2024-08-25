from django.urls import path

from .views import RegisterCustomUserView, LoginCustomUserView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterCustomUserView.as_view(), name='register'),
    path('login/', LoginCustomUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
