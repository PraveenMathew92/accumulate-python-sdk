from logging import error
import unittest
from src import json_rpc_client
from src.data.error import Error

DEFAULT_URL = 'https://testnet.accumulatenetwork.io/v1'

class JSONRPCTestCase(unittest.TestCase):
    def test_version_success(self):
        version = json_rpc_client.version(DEFAULT_URL)
        self.assertEqual(version, "v0.2.1-12-g5e55124")

    def test_get_account_success(self):
        user_adi = 'acc://8142b29062a927f87b2a4cc071bde0a31b912d6569a89e9b/ACME'
        account = json_rpc_client.get_account(user_adi, net_url=DEFAULT_URL)
        self.assertEquals(account.url, user_adi)

    def test_get_account_fail(self):
        invalid_user_adi = 'acc://8142b29062a92/ACME'
        with self.assertRaises(Error) as error:
            account = json_rpc_client.get_account(invalid_user_adi, net_url=DEFAULT_URL)