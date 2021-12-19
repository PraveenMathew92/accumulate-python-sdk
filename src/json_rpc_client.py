import json
import requests
from src.Account import Account
from src.data.error import Error

DEFAULT_URL = 'https://devnet.accumulatenetwork.io/v1'

def get_account(acc_url: str, net_url=DEFAULT_URL):
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "get",
        "params": {
            "url": acc_url
        }
    }
    response = json.loads(requests.post(net_url, json=payload).content)
    is_error = 'error' in response
    if(is_error):
        code = response['error']['code']
        message = response['error']['message']
        data = response['error']['data']
        error = Error(code, message, data)
        raise error

    account_type = response['result']['type']
    account_url = response['result']['data']['url']
    account_balance = response['result']['data']['balance']
    account = Account(account_type, account_url, account_balance)
    return account


def faucet(acc_url: str, net_url=DEFAULT_URL):
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "faucet",
        "params": {
            "url": acc_url
        }
    }
    response = json.loads(requests.post(net_url, json=payload).content)
    is_error = 'error' in response
    if(is_error):
        code = response['error']['code']
        message = response['error']['message']
        data = response['error']['data']
        error = Error(code, message, data)
        raise error
    tx_id = response['result']['data']['txid']
    return tx_id


def version(net_url=DEFAULT_URL) -> str:
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "version"
    }
    response = requests.post(net_url, json=payload)
    version = json.loads(response.content)['result']['data']['version']
    return version

if __name__ == '__main__':
    # faucet('acc://8142b29062a927f87b2a4cc071bde0a31b912d6569a89e9b/ACME', net_url='https://testnet.accumulatenetwork.io/v1')
    print(faucet('acc://69a89e9b/ACME', net_url='https://testnet.accumulatenetwork.io/v1'))
    # faucet('acc://8669bca56b7931ea4af487ac8173468099470e89ba4e5df4/ACME')
    print(get_account('acc://8142b29062a927f87b2a4cc071bde0a31b912d6569a89e9b/ACME', net_url='https://testnet.accumulatenetwork.io/v1'))
    print(version())
    # get_account('acc://8669bca56b7931ea4af487ac8173468099470e89ba4e5df4/ACME')