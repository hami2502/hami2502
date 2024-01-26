import yfinance as yf
import sys
import json

# JSON-Datei einlesen
with open('stocks.json', 'r') as file:
    stocks = json.load(file)
    
for stock in stocks:
    ticker_symbol = stock['ticker']
    data = yf.download(ticker_symbol, period="1y")
    data['MA200'] = data['Close'].rolling(window=200).mean()
    latest_close = data['Close'].iloc[-1]
    latest_ma200 = data['MA200'].iloc[-1]
    print(f"Aktueller Kurs von {ticker_symbol}: {latest_close}")
    print(f"MA200 von {ticker_symbol}: {latest_ma200}")
    
    percent_difference = ((latest_close - latest_ma200) / latest_ma200) * 100
    if percent_difference > 3:
        print(f"Kaufen")
    elif percent_difference < -3:
        print(f"Verkaufen")
    else:
        print(f"Halten")