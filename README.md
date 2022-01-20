# Python SDK for Accumulate Blockchain (WIP)

## Accumulate Blockchain API

Accumulate Blockchain uses the json rpc for communication with the mainnet. [Accumulate API Reference](https://docs.accumulatenetwork.io/accumulate/developers/api/api-reference#token-account) 

The sdk is a wrapper over the same.

## Running the tests

`$ python -m unittest -v test/test_json_rpc_client.py`

The expected output is

```
test_faucet_fail (test.test_json_rpc_client.JSONRPCTestCase) ... ok
test_faucet_success (test.test_json_rpc_client.JSONRPCTestCase) ... ok
test_get_account_fail (test.test_json_rpc_client.JSONRPCTestCase) ... ok
test_get_account_success (test.test_json_rpc_client.JSONRPCTestCase) ... ok
test_version_success (test.test_json_rpc_client.JSONRPCTestCase) ... ok
```