from django.contrib import admin
from .models import Game, Move
from django.utils.html import format_html
from django.urls import path
from django.template import Template, Context
from django.template.response import TemplateResponse
from client.modules import stats, graph
import chessdotcom
from django.http import JsonResponse

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('stats/result', self.result),
            path('stats/eco', self.eco),
            path('stats/country', self.country),
            path('stats/rating', self.rating),
            path('tomove', self.tomove),
        ]
        return my_urls + urls

    def tomove(self, request):
        context = dict(
            self.admin_site.each_context(request),
        )
        to_move = chessdotcom.get_player_current_games_to_move('seiftn')
        result = []
        if len(to_move.games):
            for m in to_move.games:
                result.append(m.url)
        return JsonResponse(result,safe=False)

    def country(self, request):
        context = dict(
            self.admin_site.each_context(request),
            games_per_countries=stats.get_games_per_country()
        )
        return TemplateResponse(request, 'stats/country.html', context)

    def rating(self, request):
        context = dict(
            self.admin_site.each_context(request),
            games_per_rating=stats.get_games_per_rating_100()
        )
        return TemplateResponse(request, 'stats/rating.html', context)

    def result(self, request):
        img = graph.get_game_results_graph(1, 1)
        context = dict(
            self.admin_site.each_context(request),
            games_per_result=stats.get_games_per_result(),
            img=img
        )
        return TemplateResponse(request, 'stats/result.html', context)

    def eco(self, request):
        context = dict(
            self.admin_site.each_context(request),
            games_per_eco=stats.get_games_by_eco()
        )
        return TemplateResponse(request, 'stats/eco.html', context)

    # Table columns
    def _opponent_country_flag(self, obj):
        template_string = f"{{% load custom_tags_filters %}}{{% show_country_flag code 16 %}}"
        template_context = {'code': obj.opponent_country}
        html = Template(template_string).render(Context(template_context))
        return format_html(html)

    _opponent_country_flag.short_description = 'C'
    _opponent_country_flag.admin_order_field = 'opponent_country'

    def _eco_link(self, obj):
        return format_html(
            '<a target="_blank" href="{}">{}</a>',
            obj.eco_url,
            obj.eco
        )

    _eco_link.short_description = 'ECO'
    _eco_link.admin_order_field = 'eco'

    def _game_link(self, obj):
        return format_html(
            '<a target="_blank" href="https://www.chess.com/game/live/{}"><img src="/static/img/link.png"</a>',
            obj.id
        )

    _game_link.short_description = ''

    def _game_result(self, obj):
        if obj.result == 'win':
            return format_html('<img src="/static/img/green.png">')
        elif obj.result == 'draw':
            return format_html('<img src="/static/img/yellow.png">')
        else:
            return format_html('<img src="/static/img/red.png">')

    _game_result.short_description = 'R'
    _game_result.admin_order_field = 'result'

    def _game_result_detail(self, obj):
        return obj.result_detail.title()

    _game_result_detail.short_description = 'By'
    _game_result_detail.admin_order_field = 'result_detail'

    def _game_date_time(self, obj):
        template_string = "{{ game_date | date:'d b Y'}} {{game_time | date:'H:i:s' }}"
        template_context = {'game_date': obj.game_date, 'game_time': obj.game_time}
        html = Template(template_string).render(Context(template_context))
        return format_html(html)

    _game_date_time.short_description = 'Date time'
    _game_date_time.admin_order_field = 'id'

    def _moves_number(self, obj):
        return obj.moves_number

    _moves_number.short_description = 'NMV'
    _moves_number.admin_order_field = 'moves_number'

    def _opponent_rating(self, obj):
        return obj.opponent_rating

    _opponent_rating.short_description = 'Vs'
    _opponent_rating.admin_order_field = 'opponent_rating'

    def _my_rating(self, obj):
        return obj.my_rating

    _my_rating.short_description = 'My'
    _my_rating.admin_order_field = 'my_rating'

    list_filter = ('result', 'result_detail', 'eco')
    list_display = (
        'id', '_game_date_time', '_my_rating', '_opponent_rating', '_game_result', '_game_result_detail',
        '_opponent_country_flag', '_eco_link', '_moves_number', '_game_link')

    list_per_page = 15


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    pass
