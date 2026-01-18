import requests
from core.http.base_api_client import BaseApiClient


class ApiClient(BaseApiClient):
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.access_token = None

    def set_token(self, token: str):
        self.access_token = token
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def get(self, path, **kwargs):
        url = self.base_url + path
        self._attach_request("GET", url, headers=self.session.headers)

        response = self.session.get(url, **kwargs)

        self._attach_response(response)
        return response

    def post(self, path, json=None, **kwargs):
        url = self.base_url + path
        self._attach_request("POST", url, payload=json, headers=self.session.headers)

        response = self.session.post(url, json=json, **kwargs)

        self._attach_response(response)
        return response

    def put(self, path, json=None, **kwargs):
        url = self.base_url + path
        self._attach_request("PUT", url, payload=json, headers=self.session.headers)

        response = self.session.put(url, json=json, **kwargs)

        self._attach_response(response)
        return response

    def delete(self, path, **kwargs):
        url = self.base_url + path
        self._attach_request("DELETE", url, headers=self.session.headers)

        response = self.session.delete(url, **kwargs)

        self._attach_response(response)
        return response
