from django.core.management.base import BaseCommand, CommandError
import chessdotcom
import json
from datetime import datetime


class Command(BaseCommand):
    help = 'Load games in database by a monthly archive'

    def add_arguments(self, parser):
        parser.add_argument('period', type=str, help='MM/YY')

    def handle(self, *args, **options):
        def get_my_color(gdata):
            if gdata.black.username == 'Seiftn':
                return 'b'
            else:
                return 'w'

        def get_my_rating(gdata):
            if gdata.black.username == 'Seiftn':
                return gdata.black.rating
            else:
                return gdata.white.rating

        def get_opponent_rating(gdata):
            if gdata.black.username == 'Seiftn':
                return gdata.white.rating
            else:
                return gdata.black.rating

        def get_opponent_username(gdata):
            if gdata.black.username == 'Seiftn':
                return gdata.white.username
            else:
                return gdata.black.username

        def get_game_date(gdata):
            date_obj = datetime.fromtimestamp(gdata.end_time)
            return date_obj.strftime("%Y-%m-%d")

        def get_result(gdata):
            if gdata.black.username == 'Seiftn':
                return gdata.black.result
            else:
                return gdata.white.result

        listperiod = options['period'].split('/')
        data = chessdotcom.get_player_games_by_month('seiftn', listperiod[1], listperiod[0])
        formatted_rows_list = []

        for g in data.games:
            game_id = g.url.split('/')
            game_id.reverse()
            formatted_rows_list.append(
                {
                    'model': 'client.Game',
                    'pk': game_id[0],
                    'fields': {
                        'game_date': get_game_date(g),
                        'time_class': g.time_class,
                        'opponent_rating': get_opponent_rating(g),
                        'opponent_username': get_opponent_username(g),
                        'my_rating': get_my_rating(g),
                        'my_color': get_my_color(g),
                        'pgn': g.pgn,
                        'result': get_result(g),
                    }
                }
            )

        with open('client/fixtures/games_' + listperiod[1] + '_' + listperiod[0] + '.json', 'w') as jsonfile:
            json.dump(formatted_rows_list, jsonfile)
        self.stdout.write(self.style.SUCCESS('Successfully generated fixture'))
