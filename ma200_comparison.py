import yfinance as yf
import sys

# Aktiensymbol als Argument übernehmen
ticker_symbol = sys.argv[1]

# Daten von yfinance abrufen
data = yf.download(ticker_symbol, period="1y")

# Berechnen des 200-Tage-Durchschnitts
data['MA200'] = data['Close'].rolling(window=200).mean()

# Letzten verfügbaren Wert und MA200 abrufen
latest_close = data['Close'].iloc[-1]
latest_ma200 = data['MA200'].iloc[-1]

# Vergleich und Ausgabe
print(f"Aktueller Kurs von {ticker_symbol}: {latest_close}")
print(f"MA200 von {ticker_symbol}: {latest_ma200}")

percent_difference = ((latest_close - latest_ma200) / latest_ma200) * 100

# Entscheidungslogik
if percent_difference > 3:
    exit 1  # Kaufen
elif percent_difference < -3:
    exit -1. #Verkaufen
else:
    exit 0