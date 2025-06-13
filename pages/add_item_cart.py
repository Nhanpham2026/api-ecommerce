import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from config import AuthenConfig

class Add_Item_Cart:
    def __init__(self, token):
        base_url = AuthenConfig.BASE_URL
        empty_cart_endpoint = AuthenConfig.EMPTYCART_ENDPOINT
        add_item_endpoint = AuthenConfig.ADD_ITEM_ENDPOINT
        self.empty_cart_endpoint = base_url + empty_cart_endpoint
        self.add_item_endpoint = base_url + add_item_endpoint
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        print("Token in Add_Item_Cart:", token)

    def create_cart(self): #empty cart
        response = requests.post(self.empty_cart_endpoint, headers=self.headers)
        print("Cart created:", response.status_code)
        return response

    def add_item_cart(self, payload): # adding item to cart
        self.create_cart()  
        return requests.post(self.add_item_endpoint, headers=self.headers, json=payload)
   
