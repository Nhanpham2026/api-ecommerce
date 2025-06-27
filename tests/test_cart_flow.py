import pytest
from pages.auth import AuthClient
from pages.empty_cart import Empty_Cart
from pages.add_item_cart import Add_Item_Cart
from pages.get_item_cart import Get_Item_Cart

@pytest.fixture(scope="session")
def token():
    return AuthClient().get_token()

@pytest.fixture(scope="session")
def add_cart_client(token):
    return Add_Item_Cart(token)

@pytest.fixture(scope="session")
def empty_cart_client(token):
    return Empty_Cart(token)

@pytest.fixture(scope="session")
def get_cart_client(token):
    return Get_Item_Cart(token)


def test_cart_end_to_end(empty_cart_client, add_cart_client, get_cart_client):
    #empty cart
    res_empty = empty_cart_client.empty_cart()
    assert res_empty.status_code in [200, 400]
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
    #add item to cart
    res_add = add_cart_client.add_item_cart(payload)
    assert res_add.status_code == 200
    assert res_add.json()["sku"] == payload["cartItem"]["sku"]

    #get item in cart
    res_get = get_cart_client.get_item_cart()
    assert res_get.status_code == 200
    response_json = res_get.json()
    items = response_json.get("items", []) if isinstance(response_json, dict) else response_json
    assert any(item.get("sku") == payload["cartItem"]["sku"] for item in items)
