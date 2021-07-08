from django.db import models


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    game_date = models.DateTimeField('game date')
    time_class = models.CharField(max_length=10)
    opponent_color = models.CharField(max_length=1)
    opponent_rating = models.IntegerField
    opponent_username = models.CharField(max_length=1)
    my_rating = models.PositiveIntegerField
    pgn = models.TextField
