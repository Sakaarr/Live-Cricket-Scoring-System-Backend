from rest_framework import serializers
from .models import Team, Player, Match, Inning, Ball

class TeamSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'short_name', 'logo_url']

    def get_logo_url(self, obj):
        if obj.logo:
            return self.context['request'].build_absolute_uri(obj.logo.url)
        return None

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    
    class Meta:
        model = Match
        fields = '__all__'

class InningSerializer(serializers.ModelSerializer):
    batting_team = TeamSerializer()
    bowling_team = TeamSerializer()
    
    class Meta:
        model = Inning
        fields = '__all__'

class BallSerializer(serializers.ModelSerializer):
    batsman = PlayerSerializer()
    bowler = PlayerSerializer()
    
    class Meta:
        model = Ball
        fields = '__all__'