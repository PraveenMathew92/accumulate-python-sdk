import unittest
from src import json_rpc_client

DEFAULT_URL = 'https://devnet.accumulatenetwork.io/v1'

class JSONRPCTestCase(unittest.TestCase):
    def test_version_success(self):
        version = json_rpc_client.version(DEFAULT_URL)
        self.assertEqual(version, "cli-api-v1-314-g45be7aa")