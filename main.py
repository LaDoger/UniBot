# Uniswap wash trade bot by LaDoger

import time
import random
import constants as c # From constants.py file
from wallets import WALLETS # From wallets.py file
from washbot import WashBot # From washbot.py file


def main():
    """Use WashBot to randomly do trades on Uniswap."""
    
    # Can deploy as many bots here
    bot0a = WashBot(
        address=WALLETS[0]['address'], # Bot wallet address.
        private_key=WALLETS[0]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WETH, # Choose token0
        token1=c.USDT, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )
    
    bot0b = WashBot(
        address=WALLETS[0]['address'], # Bot wallet address.
        private_key=WALLETS[0]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WBTC, # Choose token0
        token1=c.DAI, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )
    
    bot1a = WashBot(
        address=WALLETS[1]['address'], # Bot wallet address.
        private_key=WALLETS[1]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WETH, # Choose token0
        token1=c.USDT, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )
    
    bot1b = WashBot(
        address=WALLETS[1]['address'], # Bot wallet address.
        private_key=WALLETS[1]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WBTC, # Choose token0
        token1=c.DAI, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )

    bot2a = WashBot(
        address=WALLETS[2]['address'], # Bot wallet address.
        private_key=WALLETS[2]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WETH, # Choose token0
        token1=c.USDT, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )
    
    bot2b = WashBot(
        address=WALLETS[2]['address'], # Bot wallet address.
        private_key=WALLETS[2]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WBTC, # Choose token0
        token1=c.DAI, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )

    bot3a = WashBot(
        address=WALLETS[3]['address'], # Bot wallet address.
        private_key=WALLETS[3]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WETH, # Choose token0
        token1=c.USDT, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )
    
    bot3b = WashBot(
        address=WALLETS[3]['address'], # Bot wallet address.
        private_key=WALLETS[3]['private_key'], # Private key of bot wallet.
        uniswap_version=3, # Choose Uniswap version
        network='polygon', # Choose network
        token0=c.WBTC, # Choose token0
        token1=c.DAI, # Choose token1
        fee=None # Choose fee (fee=3000 means 0.3% maker fee)
        )

    # Create a list of bots you want to trade with
    bots = [bot0a, bot0b, bot1a, bot1b, bot2a, bot2b, bot3a, bot3b]

    # Loop after each trade attempt
    while True:
        try:
            # Randomly choose a bot from bot_list
            random_bot = random.choice(bots)
            
            random_bot.buy_or_sell() # The main thing!!!

            # You can add complex trading logic here


            # Decide how many seconds to rest the bot
            rest = int(random.randrange(1, 42) ** 2) # 1-1764 seconds
            print(f'Bot resting for {rest} seconds...\n')
            time.sleep(rest)

        except:
            print('Error! Will try again in 10 seconds...\n')
            time.sleep(10) # Wait 10 seconds then try again


if __name__ == '__main__':
    main()
