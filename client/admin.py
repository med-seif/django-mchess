from django.contrib import admin
from .models import Game, Move
from django.utils.html import format_html
from django.urls import path
from django.template import Template, Context
from django.template.response import TemplateResponse
from client.modules import stats


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('stats/result', self.result),
            path('stats/eco', self.eco),
            path('stats/country', self.country),
            path('stats/rating', self.rating),
        ]
        return my_urls + urls

    def country(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            games_per_countries=stats.get_games_per_country()
        )
        return TemplateResponse(request, 'stats/country.html', context)

    def rating(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            games_per_rating=stats.get_games_per_rating_100()
        )

        return TemplateResponse(request, 'stats/rating.html', context)

    def result(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            games_per_result=stats.get_games_per_result()
        )

        return TemplateResponse(request, 'stats/result.html', context)

    def eco(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            games_per_eco=stats.get_games_by_eco()
        )

        return TemplateResponse(request, 'stats/eco.html', context)

    # functions for game table columns under Admin
    def opponent_country_flag(self, obj):
        template_string = f"{{% load custom_tags_filters %}}{{% show_country_flag code 16 %}}"
        template_context = {'code': obj.opponent_country}
        html = Template(template_string).render(Context(template_context))
        return format_html(html)

    def eco_link(self, obj):
        return format_html(
            '<a target="_blank" href="{}">{}</a>',
            obj.eco_url,
            obj.eco
        )

    def game_link(self, obj):
        return format_html(
            '<a target="_blank" href="https://www.chess.com/game/live/{}"><img src="/static/img/link.png"</a>',
            obj.id
        )

    def game_result(self, obj):
        if obj.result == 'win':
            return format_html('<img src="/static/img/green.png">')
        elif obj.result == 'draw':
            return format_html('<img src="/static/img/yellow.png">')
        else:
            return format_html('<img src="/static/img/red.png">')

    def game_result_detail(self, obj):
        return obj.result_detail.title()

    def get_game_date(self, obj):
        template_string = "{{ game_date | date:'d b Y' }}"
        template_context = {'game_date': obj.game_date}
        html = Template(template_string).render(Context(template_context))
        return format_html(html)

    def get_game_time(self, obj):
        template_string = "{{game_time | date:'H:i:s'}}"
        template_context = {'game_time': obj.game_time}
        html = Template(template_string).render(Context(template_context))
        return format_html(html)

    eco_link.admin_order_field = 'eco'
    opponent_country_flag.admin_order_field = 'opponent_country'

    list_display = (
        'id', 'get_game_date', 'get_game_time', 'my_rating', 'opponent_rating', 'game_result', 'game_result_detail',
        'opponent_country_flag', 'eco_link', 'moves_number', 'game_link')
    list_per_page = 15


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    pass
