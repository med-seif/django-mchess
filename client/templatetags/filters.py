import pycountry
from django import template


register = template.Library()

@register.filter(name='country_name_from_code')
def get_country_name_from_code(value):
    return pycountry.countries.get(alpha_2=value).name
