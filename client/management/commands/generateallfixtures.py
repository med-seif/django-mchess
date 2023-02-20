from django.core.management.base import BaseCommand, CommandError
from django.core import management
from chessdotcom import *
from tqdm import tqdm
from django.conf import settings
import os.path
from progress.bar import Bar

class Command(BaseCommand):
    help = 'Generates all fixtures for all archives at once'

    def handle(self, *args, **options):
        archives = get_player_game_archives(settings.PLAYER_USERNAME).archives
        bar = Bar('Current is %(index)d',fill='=', suffix='%(percent)d%%').iter(archives)
        for arch in bar:
            arch_url_data = arch.split('/')
            arch_url_data.reverse()
            # self.stdout.write("Writing from %s" % arch)
            if not os.path.isfile('client/fixtures/games_' +  arch_url_data[1] + '_' + arch_url_data[0] + '.json'):
                management.call_command('generatefixture', arch_url_data[0] + '/' + arch_url_data[1])
            # else:
                # self.stdout.write(self.style.SUCCESS('Skipping ' + arch_url_data[1] + '/' + arch_url_data[0]))

        self.stdout.write(self.style.SUCCESS('Fixtures were created successfully'))
