import yaml
import xml.etree.ElementTree as ET
import requests
from models.site import Site
from models.request import Request


# Class
class Url_Tableau():

    # ----------------------  Methods  ----------------------
    # GET
    async def GET(self, request: Request):
        # Initialize variables
        url = request.url
        body = request.body
        headers = request.headers

        # Request to site
        response = requests.get(url, body, headers)

        return response

    # POST
    async def POST(self, request: Request):

        # Initialize variables
        url = request.url
        body = request.body
        headers = request.headers

        # Request to site
        response = requests.post(url, body, headers)

        return response

    # ----------------------  Methods  ----------------------

    # ----------------------    URL    ----------------------
    # Login
    async def login(self, site: Site):
        # Open settings
        with open('settings/api_version_tableau.yaml') as settings:
            server_settings = yaml.load(settings, Loader=yaml.FullLoader)

        # Initialize variables
        server = site.server
        site_name = site.site_name
        version = server_settings['server'][server]['version']
        pat_name = server_settings['server'][server]['pat_name']
        pat_secret = server_settings['server'][server]['pat_secret']

        # Url
        url = f'https://{server}/api/{version}/auth/signin'

        # Headers
        header = None

        # Body
        body_xml = ET.Element('tsRequest')
        credentials = ET.SubElement(body_xml, 'credentials',
                                    personalAccessTokenNamee=pat_name,
                                    personalAccessTokenSecret=pat_secret)
        ET.SubElement(credentials, 'site', contentUrl=site_name)
        body = ET.tostring(body_xml)

        # Request object
        request = Request()
        request.url = url
        request.headers = header
        request.body = body

        # Request
        response = await self.POST(request)

        return response
    # ----------------------    URL    ----------------------


# Oject
url_tableau = Url_Tableau()
