import yaml
import json
from modules.CSV_to_JSON import CSV_to_JSON
from modules.user_list_to_obj import user_list_to_obj


def controllers(route, content):

    # Reading and transforming content into users dictionary
    if content["json"]:
        users = content["json"]
    elif 'file' in content['file']:
        json_content = CSV_to_JSON(content['file'])
        users = json.loads(json_content)
    elif 'file' not in content['file'] and not content['json']:
        error = 'not file or json users to proccess the request'
        return error

    # Transforming list of dict (JSON) to list of User object
    users = user_list_to_obj(users)

    # Reading routes and microservices settings file
    with open('settings/routes.yaml') as settings:
        routes_microservices = yaml.load(settings, Loader=yaml.FullLoader)

    microservice = routes_microservices['route_microservice'][route]

    # Dynamic import of microservices
    microservice_module = __import__(
        f'micro_service.{microservice}.main', fromlist=['main'])

    # Calling the microservice
    call = getattr(microservice_module, 'main')(users)

    return call
