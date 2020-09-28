from enum import Enum, auto
import json
import os
from requests import get, head, post, delete


def get_api():
    """
    :return: Default API key
    """
    module_file_path = os.path.dirname(__file__)
    conf_file_path = os.path.join(module_file_path, os.pardir, 'conf', 'conf.json')
    with open(conf_file_path) as conf:
        content = json.loads(conf.read())
    api_key =  content.get('api_key')
    assert api_key, "API key seems to be empty, check conf.json"
    return api_key


class EndPoints(Enum):
    """
    Supported endpoints
    """
    countries = auto()
    holidays = auto()
    languages = auto()
    workday = auto()


class Response:
    """
    Encapsulation http status code and http content as json
    """
    def __init__(self, api_response):
        self.code = api_response.status_code
        self.raw_content = api_response.content.decode()
        self.__content_decoded = '{}' if self.raw_content == '' else self.raw_content
        self.json_content = json.loads(self.__content_decoded)


class APIClient:
    """
    Encapsulating URL, API & Endpoints into client
    """
    def __init__(self, endpoint, version="v1", api_key=None, default_api_key=True):
        """
        :param endpoint: rest endpoint
        :param version: version on implementaion
        :param api_key: api key for auth
        :param default_api_key: specify to use default api key
        """
        self.endpoint = endpoint
        self.version = version
        base_url = "https://holidayapi.com/"
        self._validate_endpoint()
        self.endpoint_url = base_url + version + '/' + endpoint.name
        if default_api_key:
            self.api_key = get_api()
        else:
            self.api_key = api_key

    def _validate_endpoint(self):
        # check endpoint is supported
        assert self.endpoint in EndPoints, "Check your endpoint, Endpoint does not seems to be part of utils"

    def parameters(self, additional_parameters=None):
        """
        :param additional_parameters: parameters for http requests
        :return: additional_parameters with api key
        """
        p = {}
        p['key'] = self.api_key
        if additional_parameters:
            p.update(additional_parameters)
        return p

    def head(self, params=None):
        """
        a http call to check stats of endpoint
        """
        params = self.parameters(additional_parameters=params)
        res = head(self.endpoint_url, params=params)
        return Response(res)

    def get(self, params=None):
        """
        a http call to retrieve data for  endpoint
        """
        params = self.parameters(additional_parameters=params)
        res = get(self.endpoint_url, params=params)
        return Response(res)

    def post(self, data=None, params=None):
        """
        a http call to create resource on endpoint
        """
        params = self.parameters(additional_parameters=params)
        res = post(self.endpoint_url, data=data, params=params)
        return Response(res)

    def delete(self, params=None):
        """
        a http call to delete resource on endpoint
        """
        params = self.parameters(additional_parameters=params)
        res = delete(self.endpoint_url, params=params)
        return Response(res)
