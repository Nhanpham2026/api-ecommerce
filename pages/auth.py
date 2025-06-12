import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from config import AuthenConfig

class  AuthClient:
    def __init__(self):
        base_url=AuthenConfig.BASE_URL
        login_endpoint = AuthenConfig.LOGIN_ENDPOINT
        self.login_endpoint = base_url + login_endpoint
        self.username=AuthenConfig.N_USERNAME
        self.password=AuthenConfig.PASSWORD

    def get_token(self):
        payload = {
            "username": self.username,
            "password": self.password,
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(self.login_endpoint, headers=headers, json=payload)
        if response.status_code == 200:
            return response.text.strip().replace('"', '')
        else:
            return None   

    def login(self, payload, headers=None):
        if headers is None:
            headers = {"Content-Type": "application/json"}
        response = requests.post(self.login_endpoint, headers=headers, json=payload)
        return response
