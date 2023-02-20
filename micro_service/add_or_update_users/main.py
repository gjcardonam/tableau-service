from models.url_tableau import url_tableau
from models.site import Site
from models.users import User
import yaml
import os


def main(users: list[User]):

    # ---------------------------- Initialization ----------------------------
    # Microservice settings
    microservice_name = os.path.basename(os.path.dirname(__file__))
    with open('settings/microservices.yaml') as settings:
        microservice = yaml.load(settings, Loader=yaml.FullLoader)[
            microservice_name]

    # Dynamic import of modules
    modules_lib = dict()
    for module in microservice['modules']:
        modules_lib[module] = __import__(
            f'modules.{module}', fromlist=[module])

    # ---------------------------- Initialization ----------------------------

    # ----------------------------    Algorithm   ----------------------------
    # Users backups
    sites = microservice['sites']
    users = getattr(modules_lib['users_backups'],
                    'users_backups')(users, sites)

    # Order users
    users.sort(key=lambda user: (user.server is None, user.server))
    users.sort(key=lambda user: (user.site is None, user.site))

    for user in users:

        # Login tableau
        site = Site()
        site.server = user.server
        site.site_name = user.site

        url_tableau.login(site)

    return 'hola mundo'
    # ----------------------------    Algorithm   ----------------------------
