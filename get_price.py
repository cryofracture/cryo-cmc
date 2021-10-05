from coinmarketcapapi import CoinMarketCapAPI
from dotenv import load_dotenv
import argparse
import os

load_dotenv()


class CryptoQuote:
    def __init__(self, symbol, currency):
        symbol = symbol.upper()
        currency = currency.upper()
        self.quote = cmc.cryptocurrency_quotes_latest(symbol=str(symbol), convert=str(currency))
        self.price = self.quote.data[f'{symbol}']['quote'][f'{currency}']['price']
        self.symbol = str(symbol)
        self.circulating = self.quote.data[f'{symbol}']['circulating_supply']
        self.max = self.quote.data[f'{symbol}'].get('max_supply', 0) or 0
        self.market_cap = self.quote.data[f'{symbol}']['quote'][f'{currency}']['fully_diluted_market_cap']
        

    def __str__(self): 
        return f"Current quote for {self.symbol}: \nCurrent Price: ${self.price} \n" \
                f"Total Circulating Supply: {self.circulating:,} \n" \
                f"Max Supply of Token: {self.max:,} \n" \
                f"Market Cap of Token: ${self.market_cap:,}" 

if __name__ == "__main__":
    CMC_API_KEY = os.environ['CMC_API_KEY']

    cmc = CoinMarketCapAPI(CMC_API_KEY)
    parser = argparse.ArgumentParser(description="CoinmarketCap API tool to get a crypto qutoe ASAP.")
    parser.add_argument("--symbol", '-s', help="Which crypto symbol to check.", type=str, required=True, dest='symbol')
    parser.add_argument("--currency", '-c', help="Which fiat currency to convert to.", type=str, required=False, dest='currency')
    parser.add_argument("--status", "-st", help="Status of airdrop. Can be:\nended\nongoing\nupcoming\n", type=str, required=False, dest='status')

    args = parser.parse_args()

    new_quote = CryptoQuote(args.symbol, args.currency)

    print(new_quote)