from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    logo = models.ImageField(
        upload_to='team_logos/',
        blank=True,
        null=True,
        help_text="Upload team logo image"
    )

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_captain = models.BooleanField(default=False)
    is_wicket_keeper = models.BooleanField(default=False)

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)
    date = models.DateTimeField()
    toss_winner = models.ForeignKey(Team, related_name='toss_wins', null=True, on_delete=models.SET_NULL)
    toss_decision = models.CharField(max_length=10, choices=[('bat', 'Bat'), ('field', 'Field')], null=True)
    status = models.CharField(max_length=20, default='scheduled')

class Inning(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    batting_team = models.ForeignKey(
        Team, 
        related_name='batting_innings',  # Unique name for batting team relationship
        on_delete=models.CASCADE
    )
    bowling_team = models.ForeignKey(
        Team, 
        related_name='bowling_innings',  # Unique name for bowling team relationship
        on_delete=models.CASCADE
    )
    inning_number = models.IntegerField()
    total_runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs_completed = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
    is_completed = models.BooleanField(default=False)

class Ball(models.Model):
    inning = models.ForeignKey(Inning, on_delete=models.CASCADE)
    over_number = models.IntegerField()
    ball_number = models.IntegerField()
    batsman = models.ForeignKey(Player, related_name='batted_balls', on_delete=models.CASCADE)
    bowler = models.ForeignKey(Player, related_name='bowled_balls', on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    is_wicket = models.BooleanField(default=False)
    wicket_type = models.CharField(max_length=50, blank=True, null=True)
    extras = models.IntegerField(default=0)
    extra_type = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)