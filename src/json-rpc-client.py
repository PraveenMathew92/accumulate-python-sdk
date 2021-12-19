import json
import requests
from Account import Account

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
    response = requests.post(net_url, json=payload)
    print(json.dumps(json.loads(response.content)['result'], indent=2))


def version(net_url=DEFAULT_URL) -> str:
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "version"
    }
    response = requests.post(net_url, json=payload)
    return json.loads(response.content)['result']['data']['version']

if __name__ == '__main__':
    faucet('acc://8142b29062a927f87b2a4cc071bde0a31b912d6569a89e9b/ACME')
    # faucet('acc://8669bca56b7931ea4af487ac8173468099470e89ba4e5df4/ACME')
    # print(get_account('acc://8142b29062a927f87b2a4cc071bde0a31b912d6569a89e9b/ACME'))
    print(version())
    # get_account('acc://8669bca56b7931ea4af487ac8173468099470e89ba4e5df4/ACME')