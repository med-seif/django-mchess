from django.core.management.base import BaseCommand, CommandError
from django.core import management
import os
from django.conf import settings

class Command(BaseCommand):
    help = "Load to DB all fixtures files, many calls to built in django command loaddata"

    def handle(self, *args, **options):
        files = os.scandir(settings.PROJECT_PATH+'/client/fixtures')
        for f in files:
            management.call_command('loaddata', f.name)
        self.stdout.write(self.style.SUCCESS('Data was saved successfully in database'))
