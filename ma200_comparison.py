import yfinance as yf
import sys
import json

# MACD und Signal Linie berechnen
def calculate_macd(data):
    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

# JSON-Datei einlesen
with open('stocks.json', 'r') as file:
    stocks = json.load(file)

for stock in stocks:
    ticker_symbol = stock['ticker']
    data = yf.download(ticker_symbol, period="1y")
    data['MA200'] = data['Close'].rolling(window=200).mean()
    data['MACD'], data['Signal'] = calculate_macd(data)
    latest_close = data['Close'].iloc[-1]
    latest_ma200 = data['MA200'].iloc[-1]
    latest_macd = data['MACD'].iloc[-1]
    latest_signal = data['Signal'].iloc[-1]

    print(f"Aktueller Kurs von {ticker_symbol}: {latest_close}")
    print(f"MA200 von {ticker_symbol}: {latest_ma200}")
    print(f"MACD von {ticker_symbol}: {latest_macd}")
    print(f"Signal von {ticker_symbol}: {latest_signal}")

    percent_difference = ((latest_close - latest_ma200) / latest_ma200) * 100
    if percent_difference > 3 or (latest_macd > latest_signal):
        print(f"Kaufen")
    elif percent_difference < -3 or (latest_macd < latest_signal):
        print(f"Verkaufen")
    else:
        print(f"Halten")
