from web3 import Web3
import os

w3 = Web3(Web3.HTTPProvider(os.getenv("CHAIN_RPC_URL")))

def anchor_hash(hash_hex, account, private_key):
    tx = {
        "to": account,
        "value": 0,
        "gas": 21000,
        "gasPrice": w3.eth.gas_price,
        "nonce": w3.eth.get_transaction_count(account),
        "data": bytes.fromhex(hash_hex)
    }
    signed = w3.eth.account.sign_transaction(tx, private_key)
    return w3.eth.send_raw_transaction(signed.rawTransaction).hex()
