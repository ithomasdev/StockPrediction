# This file will use the Ticker.py file and Stock.py model to provide app.py a window to the other necessary files
from numpy import dtype
from models.Stock import Stock
import data.ticker as Ticker
import os
import dask.dataframe as df

# array of stocks
Stocks = []

# this manual array will allow this file to be psuedo dynamic
stock_symbols = ['SPY', 'AMZN']
stock_names = ['SPDR S&P 500 ETF Trust', 'Amazon.com, Inc.']

# Accessible array of Stocks
def get_stocks():
    return Stocks

# hardcoded intentionally
def set_stocks():
    for i in range(len(stock_names)):
        Stocks.append(Stock(stock_names[i], stock_symbols[i], Ticker.get_full_dataframe(stock_symbols[i])))

# uses stock_symbols array to create excel files, this method is currently archived...  
def create_data():
    for i in stock_symbols:
        Ticker.populate_data(i, 'y', 20, 2000, 1)

def set_up():
    # by default, create_data will not be called unless uncommented
    #create_data()
    set_stocks()
