import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.auth import AuthClient
import csv
import pytest

def load_csv_data(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        print("Loaded CSV data:", data)  
        return data
#get
@pytest.mark.parametrize("case", load_csv_data("data/invalid_login.csv"))
def test_invalid_login(case):
    client = AuthClient()
    payload = {
        "username": case["username"],
        "password": case["password"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = client.login(payload, headers)
    assert response.status_code == int(case["expected_status"])
