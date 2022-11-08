# Uniswap V3 Bot
![import_random](https://user-images.githubusercontent.com/60722582/188267322-1774041b-8018-4f6f-8f6e-2528b6f47ee6.jpeg)

## Intro

* Uses https://github.com/uniswap-python to wash trade a token on Uniswap.
* *Randomly* does a trade every **1-3600 seconds**.
* *Randomly* chooses to swap `token0` for `token1` or vice versa.
* *Randomly* chooses to swap **1%-10%** of token balance.
* Goal is to randomly wash trade within a Uniswap token pair to pump up volume.

## How To

* `wallets.py` is where you put your **wallet addresses** & **private keys**.
* `constants.py` is where the **RPC Endpoint URLs** and **ERC20 Token Info** are stored.
* `washbot.py` contains `class WashBot()`. You can configure it.
* `main.py` is where you initialize your bots. You can deploy as many as you want and set different logics.

## Feeding the Bots

* Once deployed, the bots will keep wash trading forever, until you halt them that is.
* Due to **Maker Fee** & **Gas**, the bots will consume **tokens** and **gas** over time.
* Send **tokens** and **gas** to the bots' wallet addresses to refuel them.