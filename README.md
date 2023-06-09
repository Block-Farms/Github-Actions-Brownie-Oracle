# Brownie Deploy Oracle/Operator Contracts

## Pre-reqs
(0) Install brownie, this repo used eth-brownie==`1.19.3`

(1) ensure network is configured in brownie, with explorer url + api key [[ref](https://eth-brownie.readthedocs.io/en/stable/network-management.html#adding-a-new-network)]
```
brownie networks add Ethereum sepolia chainid=11155111 host=YOUR_RPC_URL explorer=https://api-sepolia.etherscan.io/api
```

(2) ensure wallet doing the on-chain tx's is funded with gas

(3) Set all variables within `.env`

(4) If running a custom oracle/operator.sol, update the contract in the contracts directory

## Deploying the oracle contract
#### compile
```
brownie compile
```

#### deploy
```
brownie run scripts/deploy.py --network sepolia
```

## Incorporation into Github Actions CI/CD:
This repo can be cloned to be executed automatically on pushes/updates to the main/master branch with Github Actions. To implement this change the module source to your github cloned repo, and the following variables to your cloned repo > Settings > Secrets and variables > Actions:

RPC HTTP URL FOR BLOCKCHAIN CONNECTIVITY:
```
RPC_URL=REDACTED
```

EXLORER URL API KEY FOR CONTRACT VERIFICATION:
```
ETHERSCAN_TOKEN=REDACTED
```EXPLORER URL API KEY FOR CONTRACT VERIFICATION:
```ETHERSCAN_TOKEN=REDACTED
```

HOT WALLET PRIVATE KEY DEPLOYING THE CONTRACT
```
PRIVATE_KEY=REDACTED
```

NODE ADDRESS WHICH SERVES THE ORACLE REQUESTS TO THE CONTRACT
```
NODE_ADDRESS=REDACTED
```

WALLET ADDRESS TO OWN THE CONTRACT AFTER DEPLOYMENT & FULFILLMENT
```
OWNER_ADDRESS=REDACTED
```

The `workflow.yaml` is default set to Ethereum Sepolia, if deploying to another network, be sure to configure L25 (brownie netowks add YOUR_NETWORK...) in `.github/workflows/workflow.yaml`


