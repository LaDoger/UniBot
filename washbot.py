# Uniswap wash trade bot by LaDoger

import web3
import random
import constants as c # From constants.py file
from uniswap import Uniswap # Library from https://uniswap-python.com/

# To solve a weird error
# https://stackoverflow.com/questions/70812529/the-field-extradata-is-97-bytes-but-should-be-32-it-is-quite-likely-that-you-a
from web3.middleware import geth_poa_middleware


class WashBot():
    """A bot that randomly trades on Uniswap."""
    
    # Decide which wallet & token pair to trade.
    def __init__(self,
                 address,
                 private_key,
                 uniswap_version,
                 network,
                 token0,
                 token1,
                 fee=None
                 ):
        self.address = address
        self.private_key = private_key
        self.version = uniswap_version
        self.network = network
        self.token0 = token0[network]
        self.token1 = token1[network]
        self.fee = fee

        # To solve the weird error mentioned above
        self.w3 = web3.Web3(web3.HTTPProvider(c.RPC[network]))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.uniswap = Uniswap(
            address=address, # Bot wallet address
            private_key=private_key, # Bot wallet private key
            version=uniswap_version, # Uniswap Version
            provider=c.RPC[network], # RPC provider endpoint url
            web3=self.w3 # To solve error https://github.com/uniswap-python/uniswap-python/issues/216
        )


    def swap_token0_for_token1(self):
        """Swap 1%-10% of token0 for token1."""
        
        qty = self.uniswap.get_token_balance(
            self.token0['address']
            ) / 10 ** self.token0['decimals']
        print(f'Wallet Address: {self.address}')
        print(f'Balance of {self.token0["symbol"]}: {qty}')

        # Choose from 1% to 10.24% to swap
        portion = random.randrange(10, 32) ** 2 / 100
        print(f'Swapping {portion}% of {self.token0["symbol"]} balance...')
        portion = portion / 100
        
        amount = int(qty * 10 ** self.token0['decimals'] * portion)
        
        self.uniswap.make_trade(
            self.token0['address'],
            self.token1['address'],
            amount,
            recipient=None,
            fee=self.fee,
            slippage=None,
            fee_on_transfer=False # Uniswap V3 doesn't support fee_on_transfer
        )
        
        print(f'Swapped {amount / 10 ** self.token0["decimals"]} {self.token0["symbol"]} for {self.token1["symbol"]}.')

        
    def swap_token1_for_token0(self):
        """Swap 1%-10% of token1 for token0."""

        qty = self.uniswap.get_token_balance(
            self.token1['address']
            ) / 10 ** self.token1['decimals']
        print(f'Wallet Address: {self.address}')
        print(f'Balance of {self.token1["symbol"]}: {qty}')

        # Choose from 1% to 10.24% to swap
        portion = random.randrange(10, 32) ** 2 / 100
        print(f'Swapping {portion}% of {self.token1["symbol"]} balance...')
        portion = portion / 100

        amount = int(qty * 10 ** self.token1['decimals'] * portion)
        
        self.uniswap.make_trade(
            self.token1['address'],
            self.token0['address'],
            amount,
            recipient=None,
            fee=self.fee,
            slippage=None,
            fee_on_transfer=False # Uniswap V3 doesn't support fee_on_transfer
        )

        print(f'Swapped {amount / 10 ** self.token1["decimals"]} {self.token1["symbol"]} for {self.token0["symbol"]}.')


    def buy_or_sell(self):
        """Randomly choose to swap what for what."""

        print('Bot contemplating...')
        r = random.choice(['0for1', '1for0'])
        
        if r == '0for1':
            self.swap_token0_for_token1()
        else:
            self.swap_token1_for_token0()
