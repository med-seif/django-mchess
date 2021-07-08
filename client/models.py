from django.db import models


class Game(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    game_date = models.DateField()
    time_class = models.CharField(max_length=10)
    opponent_color = models.CharField(max_length=1)
    opponent_rating = models.PositiveIntegerField()
    opponent_username = models.CharField(max_length=50)
    my_rating = models.PositiveIntegerField()
    pgn = models.TextField()

    class Meta:
        db_table = 'game'
