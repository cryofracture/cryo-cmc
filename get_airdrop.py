from coinmarketcapapi import CoinMarketCapAPI
from dotenv import load_dotenv
import argparse
import os

load_dotenv()

class CryptoAirdrops:
    def __init__(self, symbol, status):
        symbol = symbol.upper()
        if status:
            status = status.upper()
        if status:
            self.airdrops = cmc.cryptocurrency_airdrops(symbol=str(symbol), status=status)
        else:
            self.airdrops = cmc.cryptocurrency_airdrops(symbol=str(symbol))

    def __str__(self): 
        return f"Current airdrops for {self.symbol}: \n {self.airdrops} \n" \

if __name__ == "__main__":
    CMC_API_KEY = os.environ['CMC_API_KEY']

    cmc = CoinMarketCapAPI(CMC_API_KEY)
    parser = argparse.ArgumentParser(description="CoinmarketCap API tool to get a crypto qutoe ASAP.")
    parser.add_argument("--symbol", '-s', help="Which crypto symbol to check.", type=str, required=True, dest='symbol')
    # parser.add_argument("--currency", '-c', help="Which fiat currency to convert to.", type=str, required=False, dest='currency')
    parser.add_argument("--status", "-st", help="Status of airdrop. Can be:\nended\nongoing\nupcoming\n", type=str, required=False, dest='status')

    args = parser.parse_args()

    new_airdrops = CryptoAirdrops(args.symbol, args.status)

    print(new_airdrops)