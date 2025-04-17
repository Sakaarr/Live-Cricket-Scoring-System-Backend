from rest_framework import viewsets
from .models import Team, Player, Match, Inning, Ball
from .serializers import TeamSerializer, PlayerSerializer, MatchSerializer, InningSerializer, BallSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class InningViewSet(viewsets.ModelViewSet):
    queryset = Inning.objects.all()
    serializer_class = InningSerializer

class BallViewSet(viewsets.ModelViewSet):
    queryset = Ball.objects.all()
    serializer_class = BallSerializer