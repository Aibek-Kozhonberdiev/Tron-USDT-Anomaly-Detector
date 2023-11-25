import json
import requests

USDT = "THPvaUhoh2Qn2y9THCZML3H815hhFhn5YC"


def get_objects(address: str = USDT) -> json:
    url = f"https://api.shasta.trongrid.io/v1/accounts/{address}/transactions/trc20"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
