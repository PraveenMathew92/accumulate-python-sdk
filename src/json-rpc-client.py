import json
import requests

DEFAULT_URL = 'https://devnet.accumulatenetwork.io/v1'

def get_account(acc_url: str, net_url=DEFAULT_URL):
    payload = {
        "jsonrpc": "2.0",
        "id": 0,
        "method": "token-account",
        "params": {
            "url": acc_url
        }
    }
    response = requests.post(net_url, json=payload)
    print(json.loads(response.content)['result'])


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
    print(json.loads(response.content)['result'])

if __name__ == '__main__':
    faucet('acc://8142b29062a927f87b2a4cc071bde0a31b912d6569a89e9b/ACME')
    get_account('acc://8142b29062a927f87b2a4cc071bde0a31b912d6569a89e9b/ACME')