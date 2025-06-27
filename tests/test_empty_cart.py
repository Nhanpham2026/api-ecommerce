import pytest
from pages.empty_cart import Empty_Cart
from pages.auth import AuthClient  


@pytest.fixture(scope="module")
def token():
    return AuthClient().get_token()

@pytest.fixture(scope="module")
def cart(token):
    return Empty_Cart(token)

def test_clear_cart(cart):
    response = cart.empty_cart()
    assert response.status_code in [200, 400]
