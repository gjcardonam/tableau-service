from models.url_tableau import url_tableau
from models.site import Site


def add_or_update_users(users):
    site = Site()
    site.server = 'tableau.falabella.com'
    site.site_name = 'No working'

    url_tableau.login(site)
    return 'hola mundo'
