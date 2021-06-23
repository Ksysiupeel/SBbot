import requests


class Bitcoin:

    @staticmethod
    def show_price_bitcoin():
        r = requests.get("https://blockchain.info/ticker")

        if r:
            return r.json()["PLN"]["15m"]