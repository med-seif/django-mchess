import pycountry


def get_country_name_from_code(code):
    try:
        return pycountry.countries.get(alpha_2=code).name
    except:
        return 'None'
