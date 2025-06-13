import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from config import AuthenConfig

class  Login_Client:
    def __init__(self):
        base_url=AuthenConfig.BASE_URL
        login_endpoint = AuthenConfig.LOGIN_ENDPOINT
        self.login_endpoint = base_url + login_endpoint
        self.username=AuthenConfig.N_USERNAME
        self.password=AuthenConfig.PASSWORD

    def login(self, payload, headers=None):
        if headers is None:
            headers = {"Content-Type": "application/json"}
        response = requests.post(self.login_endpoint, headers=headers, json=payload)
        return response
