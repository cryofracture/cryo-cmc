# Cryo's CMC Token Check Tool

A quickly thrown together script to search [CoinMarketCap](https://coinmarketcap.com) for info on a token symbol, converted to local currency.

# Usage:
```
usage: get_price.py [-h] --symbol SYMBOL --currency CURRENCY
```

# Returned Info:
The script will build an object with the following information for the requested token:

    Symbol
    Current Price
    Circulating Supply
    Max Supply (If applicable)
    Total Market Cap