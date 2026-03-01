from rest_framework import generics
from .models import User, Club, Player
from .serializers import UserSerializer, ClubSerializer, PlayerSerializer

# GET all users
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# GET all clubs
class ClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

# GET all players
class PlayerListAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer