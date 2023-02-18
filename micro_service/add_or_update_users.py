from models.url_tableau import url_tableau
from models.site import Site


async def add_or_update_users(users):
    site = Site()
    site.server = 'tableau.falabella.com'
    site.site_name = 'No working'

    await url_tableau.login(site)
    return 'hola mundo'
