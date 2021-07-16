from django.db import models


class Game(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    game_date = models.DateField()
    time_class = models.CharField(max_length=10)
    opponent_rating = models.PositiveIntegerField()
    opponent_username = models.CharField(max_length=50)
    opponent_country = models.CharField(max_length=2, null=True)
    my_rating = models.PositiveIntegerField()
    my_color = models.CharField(max_length=1, null=True)
    result = models.CharField(max_length=20, null=True)
    pgn = models.TextField()

    class Meta:
        db_table = 'game'
