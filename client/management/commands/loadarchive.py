from django.core.management.base import BaseCommand, CommandError
import chessdotcom
import json
import datetime
from pgn_parser import parser as pgn_parser, pgn
from pytz import timezone
from django.conf import settings


class Command(BaseCommand):
    help = 'Generates a monthly archive in JSON ready file to be loaded in database with loaddata python command'

    def add_arguments(self, parser):
        parser.add_argument('period', type=str, help='MM/YYYY, example 07/2021')

    def handle(self, *args, **options):
        def get_my_color(gdata):
            return 'b' if gdata.black.username == settings.PLAYER_USERNAME else 'w'

        def get_my_rating(gdata):
            return gdata.black.rating if gdata.black.username == settings.PLAYER_USERNAME else gdata.white.rating

        def get_opponent_rating(gdata):
            return gdata.white.rating if gdata.black.username == settings.PLAYER_USERNAME else gdata.black.rating

        def get_opponent_username(gdata):
            return gdata.white.username if gdata.black.username == settings.PLAYER_USERNAME else gdata.black.username

        def get_result_detail(gdata, pgn_parsed_data):

            def format_win_result(result, pgn_parsed_data_in):
                if result != 'win':
                    return result
                win_results = {
                    'resignation': settings.PLAYER_USERNAME + ' won by resignation',
                    'checkmate': settings.PLAYER_USERNAME + ' won by checkmate',
                    'abandonment': settings.PLAYER_USERNAME + ' won - game abandoned',
                    'time': settings.PLAYER_USERNAME + ' won on time'
                }
                termination = pgn_parsed_data_in.tag_pairs['Termination']
                for win_result_k, win_result_v in win_results.items():
                    if win_result_v == termination:
                        return win_result_k

            if gdata.black.username == 'Seiftn':
                return format_win_result(gdata.black.result, pgn_parsed_data)
            else:
                return format_win_result(gdata.white.result, pgn_parsed_data)

        # returns result summary (win, loose, draw) without details based on result detail (checkmated, resigned...)
        def get_result(gdata, pgn_parsed_data):
            draw = ('stalemate', 'insufficient', 'agreed', 'timevsinsufficient', 'repetition')
            loose = ('timeout', 'resigned', 'abandoned', 'checkmated')
            win = ('resignation', 'checkmate', 'time', 'abandonment')
            result_detail = get_result_detail(gdata, pgn_parsed_data)
            if result_detail in draw:
                return 'draw'
            if result_detail in loose:
                return 'loose'
            if result_detail in win:
                return 'win'
            return '_'

        def get_termination(pgn_parsed_data):
            return pgn_parsed_data.tag_pairs['Termination']

        def get_eco(pgn_parsed_data):
            return pgn_parsed_data.tag_pairs['ECO']

        def get_eco_url(pgn_parsed_data):
            return pgn_parsed_data.tag_pairs['ECOUrl']

        def get_game_date_time(pgn_parsed_data, utc_date_key, utc_time_key, date_time_format):
            utc_date_key = pgn_parsed_data.tag_pairs[utc_date_key]
            utc_time_key = pgn_parsed_data.tag_pairs[utc_time_key]
            date = datetime.datetime.strptime(utc_date_key + ' ' + utc_time_key, '%Y.%m.%d %H:%M:%S')
            # utc is the default timezone, we will convert from
            date = date.astimezone(timezone('US/EASTERN'))
            return date.strftime(date_time_format)

        def get_player_country(gdata):
            player_profile = chessdotcom.get_player_profile(get_opponent_username(gdata))
            country_url_api = player_profile.player.country
            country_url_api_parts = country_url_api.split('/')
            country_url_api_parts.reverse()
            return country_url_api_parts[0]

        listperiod = options['period'].split('/')
        data = chessdotcom.get_player_games_by_month('seiftn', listperiod[1], listperiod[0])
        formatted_rows_list = []

        for g in data.games:
            pgn_parsed = pgn_parser.parse(g.pgn, actions=pgn.Actions())
            game_id = g.url.split('/')
            game_id.reverse()
            formatted_rows_list.append(
                {
                    'model': 'client.Game',
                    'pk': game_id[0],
                    'fields': {
                        'time_class': g.time_class,
                        'opponent_rating': get_opponent_rating(g),
                        'opponent_username': get_opponent_username(g),
                        'my_rating': get_my_rating(g),
                        'my_color': get_my_color(g),
                        'pgn': g.pgn,
                        'result_detail': get_result_detail(g, pgn_parsed),
                        'result': get_result(g, pgn_parsed),
                        'opponent_country': get_player_country(g),
                        'termination': get_termination(pgn_parsed),
                        'eco': get_eco(pgn_parsed),
                        'eco_url': get_eco_url(pgn_parsed),
                        'game_end_date': get_game_date_time(pgn_parsed,'EndDate','EndTime','%Y-%m-%d'),
                        'game_end_time': get_game_date_time(pgn_parsed,'EndDate','EndTime','%H:%M:%S'),
                        'game_date': get_game_date_time(pgn_parsed,'UTCDate', 'UTCTime','%Y-%m-%d'),
                        'game_time': get_game_date_time(pgn_parsed,'UTCDate', 'UTCTime','%H:%M:%S'),
                    }
                }
            )

        with open('client/fixtures/games_' + listperiod[1] + '_' + listperiod[0] + '.json', 'w') as jsonfile:
            json.dump(formatted_rows_list, jsonfile)
        self.stdout.write(self.style.SUCCESS('Successfully generated fixture for ' + options['period']))
