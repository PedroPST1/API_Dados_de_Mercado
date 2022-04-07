from pip._vendor import requests
from time import sleep
from pip._vendor.requests import get
from dmapi import DMAPI

VERSION = '0.0.1'
API_BASE_URL = 'https://www.dadosdemercado.com/api/v0'


class DMAPI:

    def __init__(self, token):
        self.api_base = API_BASE_URL
        self.token = "4891f7bd974426c419b1fd0d3b67412d"

    def _build_url(self, url):
        return self.api_base + url

    def _headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.token),
        }
    
    def _get(self, url, data={}, retry=0):
        response = get(
            self._build_url(url),
            data=data,
            headers=self._headers(),
        )

        if response.status_code == 429:
            sleep(2 ** retry)
            return self._get(url, data, retry + 1)

        return response.json()

    def companies(self, ):
        url = '/companies'
        return self._get(url)
    
    print(companies())
