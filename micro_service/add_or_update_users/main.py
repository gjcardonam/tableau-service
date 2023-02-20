from models.url_tableau import url_tableau
from models.site import Site
from models.users import User
import yaml
import os


def add_or_update_users(users: list[User]):

    # Microservice settings
    with open('settings/microservices.yaml') as settings:
        microservices = yaml.load(settings, Loader=yaml.FullLoader)

    # Dynamic import of modules
    modules_lib = dict()
    microservice = os.path.basename(os.path.dirname(__file__))
    for module in microservices[microservice]['modules']:
        modules_lib[module] = __import__(
            f'modules.{module}', fromlist=[module])

    # Users backups
    servers = microservices[microservice]['servers']
    users = getattr(modules_lib['users_backups'],
                    'users_backups')(users, servers)

    # Order users
    users.sort(key=lambda user: (user.server is None, user.server))

    site = Site()
    site.server = 'tableau.falabella.com'
    site.site_name = 'No working'

    url_tableau.login(site)
    return 'hola mundo'
