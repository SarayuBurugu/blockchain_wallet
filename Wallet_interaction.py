from web3 import Web3

RPC_URL = "https://eth-sepolia.g.alchemy.com/v2/sTcYQSXfGu3TwIm1IF5Bc"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

print("Connected:", web3.is_connected())

PRIVATE_KEY = "231a11b331684ee3eed72339d6939e65dd61d04b8a55cc8af397655840adf59e"
account = web3.eth.account.from_key(PRIVATE_KEY)

print("Wallet Address:", account.address)
wallet_address = account.address


balance = web3.eth.get_balance(account.address)
print("Balance (ETH):", web3.from_wei(balance, 'ether'))


transaction = {
    "nonce": web3.eth.get_transaction_count(wallet_address),
    "to": "0x000000000000000000000000000000000000dead",
    "value": web3.to_wei(0.001, "ether"),
    "gas": 21000,
    "gasPrice": web3.eth.gas_price,
    "chainId": 11155111  # Sepolia chain ID
}

print("\nPrepared Transaction (not sent):")
print(transaction)