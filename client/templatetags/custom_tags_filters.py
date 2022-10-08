from django import template
from client.modules.proxy import pcountry_proxy

register = template.Library()


@register.inclusion_tag('country.html')
def show_country_flag(code, w=24):
    country_name = pcountry_proxy.get_country_name_from_code(code)
    if 'None' == country_name:
        return {
            'country_code': code,
        }
    return {
        'country_name': country_name,
        'country_flag': "https://flagcdn.com/" + str(w) + 'x12/' + code.lower() + ".png" if country_name != 'None' else '#'
    }

