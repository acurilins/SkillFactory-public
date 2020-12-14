import requests
import json
from config import keys


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f'Chosen currencies are the same {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f"Couldn't recognize currency {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f"Couldn't recognize currency {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Couldn't recognize the amount {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base * amount
        return total_base
