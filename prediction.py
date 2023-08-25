import yfinance as yf 
import pandas as pd 

index = yf.Ticker('PLACE_TICKER_HERE')
index = index.history(period='max')
print(index)