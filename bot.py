from binance import Client

class BinanceClient:
    def __init__(self, key: str, secret: str):
        self.__client = Client(key, secret, testnet = True)
        self.__client.API_URL = "https://testnet.binancefuture.com/fapi"

    def create_order(self, symbol: str, side: str, kind: str, quantity: float):
        return self.__client.futures_create_order(
            symbol = symbol,
            side = side,
            type = kind,
            quantity = quantity)
        