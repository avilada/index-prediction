import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt

def print_ticker():
    '''print function for index dataframe.'''
    print(ticker_index)

def print_index():
    '''print function for the index of the dataframe.'''
    print(ticker_index.index)

def print_close_visual():
    '''print function for a visual of the dataframe.'''
    print(ticker_index.plot.line(y='Close'))
    plt.show(block=True)

ticker_index = yf.Ticker('^GSPC')
ticker_index = ticker_index.history(period='max')
print_close_visual()