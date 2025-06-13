import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from pages.add_item_cart import Add_Item_Cart
from pages.get_item_cart import Get_Item_Cart
from pages.auth import AuthClient  


@pytest.fixture(scope="module")
def token():
    return AuthClient().get_token()

@pytest.fixture(scope="module")
def add_cart(token):
    return Add_Item_Cart(token)

@pytest.fixture(scope="module")
def get_cart(token):
    return Get_Item_Cart(token)

#Add 1 item thanh cong va kiem tra resonse
def test_add_and_get_item_cart(add_cart, get_cart):
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
    add_response = add_cart.add_item_cart(payload)
    assert add_response.status_code == 200

    get_response = get_cart.get_item_cart()
    assert get_response.status_code == 200
    response_json = get_response.json()
    items = response_json.get("items", []) if isinstance(response_json, dict) else response_json
    assert any(item.get("sku") == payload["cartItem"]["sku"] for item in items)