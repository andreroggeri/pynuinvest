import json
from typing import Optional
from urllib.parse import urlencode

import requests


class NuInvest:

    def __init__(self, solverr_url='http://localhost:8191/v1'):
        self._solverr_url = solverr_url
        self._auth_token = None

    def authenticate(self, login: str, password: str, device_uid: str, otp_code: Optional[str] = None):
        body = {
            'username': login,
            'password': password,
            'device_uid': device_uid,
            'grant_type': 'password',
            'client_id': '3f1c7db528cc4bfc9c817f918d11748a',
        }
        if otp_code:
            body['otp_code'] = otp_code

        response = self._make_post('https://api.easynvest.com.br/auth/v3/security/token', body)

        self._auth_token = response['access_token']

    def get_investment_data(self) -> dict:
        if self._auth_token is None:
            raise Exception('Authenticate before requesting data')

        return self._make_get('https://www.nuinvest.com.br/api/samwise/v2/custody-position')

    def _make_post(self, url: str, inner_body: dict) -> dict:
        body = {
            "cmd": "request.post",
            "url": url,
            "headers": {
                "content-type": "application/x-www-form-urlencoded"
            },
            "postData": urlencode(inner_body),
            "returnRawHtml": True
        }

        response = requests.post(self._solverr_url, json=body)
        content = response.json()['solution']['response']

        return json.loads(content)

    def _make_get(self, url: str) -> dict:
        body = {
            "cmd": "request.get",
            "url": url,
            "headers": {
                'Authorization': f'Bearer {self._auth_token}'
            },
            "returnRawHtml": True
        }

        response = requests.post(self._solverr_url, json=body)
        content = response.json()['solution']['response']

        return json.loads(content)
