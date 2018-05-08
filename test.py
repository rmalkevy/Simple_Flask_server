import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract


# compile your smart contract with truffle first
truffleFile = json.load(open('truffle/build/contracts/Greet.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']

# web3.py instance
w3 = Web3(HTTPProvider("http://localhost:9545/"))


# Instantiate and deploy contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
contract_instance = w3.eth.contract(abi=abi, address=contract_address, ContractFactoryClass=ConciseContract)

# Getters + Setters for web3.eth.contract object
print('Contract value: {}'.format(contract_instance.greet()))
contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
print('Setting value to: Nihao')
print('Contract value: {}'.format(contract_instance.greet()))
