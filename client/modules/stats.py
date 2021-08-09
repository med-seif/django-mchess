from client.models import Game
from django.db.models import Count
from django.db.models import F, Q, Avg, Min, Max


def get_games_per_country():
    return Game.objects.values('opponent_country').annotate(
        count=Count('opponent_country'),
        avg_opponent_rating=Avg('opponent_rating'),
        count_win=Count('opponent_country', filter=Q(result='win')),
        count_loose=Count('opponent_country', filter=Q(result='loose')),
        count_draw=Count('opponent_country', filter=Q(result='draw'))
    ).order_by('-count')


def get_games_per_rating_100():
    return Game.objects.aggregate(
        min_rating=Min('opponent_rating'),
        max_rating=Max('opponent_rating'),
        avg=Avg('opponent_rating'),
        avg_win=Avg('opponent_rating', filter=Q(result='win')),
        avg_loose=Avg('opponent_rating', filter=Q(result='loose')),
        avg_draw=Avg('opponent_rating', filter=Q(result='draw')),
        _0=(Count('id', filter=Q(opponent_rating__lt=500))),
        _500=(Count('id', filter=Q(opponent_rating__gte=500, opponent_rating__lt=600))),
        _500_avg=(Avg('opponent_rating', filter=Q(opponent_rating__gte=500, opponent_rating__lt=600))),
        _600=(Count('id', filter=Q(opponent_rating__gte=600, opponent_rating__lt=700))),
        _600_avg=(Avg('opponent_rating', filter=Q(opponent_rating__gte=600, opponent_rating__lt=700))),
        _700=(Count('id', filter=Q(opponent_rating__gte=700, opponent_rating__lt=800))),
        _700_avg=(Avg('opponent_rating', filter=Q(opponent_rating__gte=700, opponent_rating__lt=800))),
        _800=(Count('id', filter=Q(opponent_rating__gte=800, opponent_rating__lt=900))),
        _800_avg=(Avg('opponent_rating', filter=Q(opponent_rating__gte=800, opponent_rating__lt=900))),
        _900=(Count('id', filter=Q(opponent_rating__gte=900, opponent_rating__lt=1000))),
        _900_avg=(Avg('opponent_rating', filter=Q(opponent_rating__gte=900, opponent_rating__lt=1000))),
        _1000=(Count('id', filter=Q(opponent_rating__gte=1000, opponent_rating__lt=1100))),
        _1000_avg=(Avg('opponent_rating', filter=Q(opponent_rating__gte=1000, opponent_rating__lt=1100))),
        _1100=(Count('id', filter=Q(opponent_rating__gte=1100, opponent_rating__lt=1200))),
        _1100_avg=(Avg('opponent_rating', filter=Q(opponent_rating__gte=1100, opponent_rating__lt=1200))),
        _1200=(Count('id', filter=Q(opponent_rating__gte=1200)))
    )


def get_games_by_eco():
    return Game.objects.values('eco').annotate(
        count=Count('eco'),
        avg_opponent_rating=Avg('opponent_rating'),
        count_win=Count('eco', filter=Q(result='win')),
        count_win_white=Count('eco', filter=Q(result='win',my_color='w')),
        count_win_black=Count('eco', filter=Q(result='win',my_color='b')),
        count_loose=Count('eco', filter=Q(result='loose')),
        count_loose_white=Count('eco', filter=Q(result='loose',my_color='w')),
        count_loose_black=Count('eco', filter=Q(result='loose',my_color='b')),
        count_draw=Count('eco', filter=Q(result='draw'))
    ).order_by('-count')


def get_games_per_result():
    return Game.objects.aggregate(
        # win
        count_win_checkmate=Count('id', filter=Q(result_detail='checkmate')),
        count_win_time=Count('id', filter=Q(result_detail='time')),
        count_win_resignation=Count('id', filter=Q(result_detail='resignation')),
        count_win_abandonment=Count('id', filter=Q(result_detail='abandonment')),
        # loose
        count_loose_checkmated=Count('id', filter=Q(result_detail='checkmated')),
        count_loose_timeout=Count('id', filter=Q(result_detail='timeout')),
        count_loose_resigned=Count('id', filter=Q(result_detail='resigned')),
        count_abandoned=Count('id', filter=Q(result_detail='abandoned')),
        # draw
        count_draw_agreed=Count('id', filter=Q(result_detail='agreed')),
        count_draw_insufficient=Count('id', filter=Q(result_detail='insufficient')),
        count_draw_stalemate=Count('id', filter=Q(result_detail='stalemate')),
        count_draw_timevsinsufficient=Count('id', filter=Q(result_detail='timevsinsufficient')),
        count_draw_repetition=Count('id', filter=Q(result_detail='repetition'))
    )
