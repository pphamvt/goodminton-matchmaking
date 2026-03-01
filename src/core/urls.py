from django.urls import path
from .views import UserListAPIView, ClubListAPIView, PlayerListAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('clubs/', ClubListAPIView.as_view(), name='club-list'),
    path('players/', PlayerListAPIView.as_view(), name='player-list'),
]