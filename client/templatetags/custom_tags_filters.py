import pycountry
from django import template

register = template.Library()

@register.inclusion_tag('country.html')
def show_country_flag(code):
    try:
        return {
            'country_name': pycountry.countries.get(alpha_2=code).name,
            'country_code': code
        }
    except:
        return {
            'country_name': '',
            'country_code': ''
        }

