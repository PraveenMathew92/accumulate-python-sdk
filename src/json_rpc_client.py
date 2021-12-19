import json
import requests
from src.Account import Account
from src.data.error import Error

DEFAULT_URL = 'https://devnet.accumulatenetwork.io/v1'

def __get_result_from_json_rpc_response(response):
    body = json.loads(response.content)
    is_error = 'error' in body
    if(is_error):
        code = body['error']['code']
        message = body['error']['message']
        data = body['error']['data']
        error = Error(code, message, data)
        raise error
    return body['result']

def get_account(acc_url: str, net_url=DEFAULT_URL):
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "url": acc_url
        }
    }
    response = requests.post(net_url, json=payload)
    result = __get_result_from_json_rpc_response(response)

    account_type = result['type']
    account_url = result['data']['url']
    account_balance = result['data']['balance']
    account = Account(account_type, account_url, account_balance)
    return account


def faucet(acc_url: str, net_url=DEFAULT_URL) -> str:
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "faucet",
        "params": {
            "url": acc_url
        }
    }
    response = requests.post(net_url, json=payload)
    result = __get_result_from_json_rpc_response(response)

    tx_id = result['data']['txid']
    return tx_id


def version(net_url=DEFAULT_URL) -> str:
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "version"
    }
    response = requests.post(net_url, json=payload)
    result = __get_result_from_json_rpc_response(response)
    version = result['data']['version']
    return version
