import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from config import AuthenConfig

class Empty_Cart:
    def __init__(self, token):
        base_url = AuthenConfig.BASE_URL
        emptycart_endpoint = AuthenConfig.EMPTYCART_ENDPOINT
        self.emptycart_endpoint = base_url + emptycart_endpoint
        self.token = token

    def empty_cart(self):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.post(self.emptycart_endpoint, headers=headers)
        return response
