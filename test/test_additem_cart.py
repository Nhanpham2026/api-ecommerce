import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from pages.add_item_cart import Add_Item_Cart
from pages.auth import AuthClient  


@pytest.fixture(scope="module")
def token():
    return AuthClient().get_token()

@pytest.fixture(scope="module")
def cart(token):
    return Add_Item_Cart(token)

#Add 1 item thanh cong va kiem tra resonse
def test_add_item_cart(cart):
    payload = {
                    "cartItem": {
                        "sku": "bto_virtual_vehicle",
                        "qty": 1,
                        "name": "BTO name",
                        "price": 10,
                        "extension_attributes": {
                            "grade": "grade",
                            "model_name": "model name",
                            "short_description": "short description",
                            "color_label": "color label",
                            "bto_configuration": "bto configuration",
                            "bto_price": 5,
                            "bto_name": "bto name"
                        }
                    }
                }
    response = cart.add_item_cart(payload)
    assert response.status_code in [200]
    assert response.json()["sku"] == payload["cartItem"]["sku"]

#Add 1 item thanh cong va qty it nhat la 1
def test_add_item_cart_qty(cart):
    payload = {
                    "cartItem": {
                        "sku": "bto_virtual_vehicle",
                        "qty": 0,
                        "name": "BTO name",
                        "price": 10,
                        "extension_attributes": {
                            "grade": "grade",
                            "model_name": "model name",
                            "short_description": "short description",
                            "color_label": "color label",
                            "bto_configuration": "bto configuration",
                            "bto_price": 5,
                            "bto_name": "bto name"
                        }
                    }
                }
    response = cart.add_item_cart(payload)
    assert response.status_code in [200]
    