import yaml
import json
from modules.CSV_to_JSON import CSV_to_JSON


async def router(route, content):

    # Reading and transforming content into users dictionary
    if content["json"]:
        users = content["json"]
    elif 'file' in content['file']:
        json_content = CSV_to_JSON(content['file'])
        users = json.loads(json_content)
    elif 'file' not in content['file'] and not content['json']:
        error = 'not file or json users to proccess the request'
        return error

    # Reading routes and microservices settings file
    with open('settings/routes.yaml') as settings:
        routes_microservices = yaml.load(settings, Loader=yaml.FullLoader)

    microservice = routes_microservices['route_microservice'][route]

    # Dynamic import of microservices
    microservice_module = __import__(
        f'micro_service.{microservice}', fromlist=[microservice])

    # Calling the microservice
    call = await getattr(microservice_module, microservice)(users)

    return call
