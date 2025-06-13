import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from config import AuthenConfig

class Get_Item_Cart:
    def __init__(self, token):
        self.token = token
        base_url = AuthenConfig.BASE_URL
        get_cart_item_endpoint = AuthenConfig.GET_CART_ITEM_ENDPOINT
        self.get_cart_item_endpoint = base_url + get_cart_item_endpoint

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get_item_cart(self):
        response = requests.get(self.get_cart_item_endpoint, headers=self.headers)
        return response


