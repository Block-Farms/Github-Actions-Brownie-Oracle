#!/usr/bin/env python3
import os
from brownie import accounts, Operator, Oracle

def main():
    '''Load your Ethereum account'''
    deployer = accounts.add(os.getenv('PRIVATE_KEY'))

    '''LINK TOKEN ADDRESSES & EXPLORER BASE URL'''
    chosen_chain_id = os.getenv('CHAIN_ID')
    if chosen_chain_id == '1': # ETH Mainnet
        link_token_address = '0x514910771AF9Ca656af840dff83E8264EcF986CA'
        explorer_url = 'https://etherscan.io/address'
    elif chosen_chain_id == '11155111': # ETH Sepolia
        link_token_address = '0x779877A7B0D9E8603169DdbD7836e478b4624789'
        explorer_url = 'https://sepolia.etherscan.io/address'
    elif chosen_chain_id == '137': # POLY Mainnet
        link_token_address = '0xb0897686c545045aFc77CF20eC7A532E3120E0F1'
        explorer_url = 'https://polygonscan.com/address'
    elif chosen_chain_id == '80001': # POLY Mumbai
        link_token_address = '0x326C977E6efc84E512bB9C30f76E30c160eD06FB'
        explorer_url = 'https://mumbai.polygonscan.com/address'
    elif chosen_chain_id == '42161': # ARB Mainnet
        link_token_address = '0xf97f4df75117a78c1A5a0DBb814Af92458539FB4'
        explorer_url = 'https://arbiscan.io/address'

    '''Deploy the contract'''
    try:
        chosen_contract = os.getenv('CONTRACT_NAME')
        if chosen_contract == 'OPERATOR':
            my_contract = Operator.deploy(link_token_address,deployer,{'from': deployer}, publish_source=True)
        elif chosen_contract == 'ORACLE':
            my_contract = Oracle.deploy(link_token_address,{'from': deployer}, publish_source=True)
        # Print the contract address
        print(f'\nContract deployed at: {my_contract.address}')
        print(f'Explorer URL: {explorer_url}/{my_contract.address}')
    except error as e:
        print(f'Contract deployment & verification failed with error: {e}')

        # if contract failed to verify (ex: polygon mainnet), delete and re-add network in brownie networks
        brownie_network_name = os.getenv('NETWORK_NAME')
        brownie_network_sub_name = os.getenv('NETWORK_SUB_NAME')
        rpc_url = os.getenv('RPC_URL')
        explorer_api_url = os.getenv('EXPLORER_API_URL')

        delete_brownie_network = subprocess.getoutput(f'brownie networks delete {brownie_network_sub_name}')
        add_brownie_network = subprocess.getoutput(f'brownie networks add {brownie_network_name} {brownie_network_sub_name} chainid={chosen_chain_id} host={rpc_url} explorer={explorer_api}')
        continue # retry try block

     '''Whitelist node address with oracle contract'''
    node_address = os.getenv('NODE_ADDRESS')
    if chosen_contract == 'OPERATOR':
        my_contract.setAuthorizedSenders([node_address], {'from': deployer})
    elif chosen_contract == 'ORACLE':
        my_contract.setFulfillmentPermission(node_address, True, {'from': deployer})

    '''
    Transfer ownership away from deployer/hot wallet
    Intended wallet owner address of the contract
    '''
    owner_address = os.getenv('OWNER_ADDRESS')
    print(f'Transferring ownership of contract to: {owner_address}')
    my_contract.transferOwnership(owner_address, {'from': deployer})
