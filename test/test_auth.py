# tests/test_auth.py
#with valid
def test_get_token_success(access_token):
    assert access_token is not None
    assert isinstance(access_token, str)
    assert len(access_token) > 10

#with invalid
def test_get_token_success(access_token):
    assert access_token is not None
    assert isinstance(access_token, str)
    assert len(access_token) > 10
