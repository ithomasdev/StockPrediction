import yfinance as yf
import pandas as pd
import dask.dataframe as dd
from pandas_datareader import data as pdr
from dask.dataframe import from_pandas

# get dataframe using folder and stock name
# takes csv file and reads + returns the dataframe
def get_dataframe(symbol):
    return

# create excel file using dask and yfinance
# needs to have a time interval set by default
# timeStart and timeEnd are for dates
def create_excel(symbol, timeStart, timeEnd):

    #get dataframe for pandas
    pd = pdr.get_data_yahoo(symbol, start=timeStart, end=timeEnd)
    
    #convert from pandas to dask dataframe
    df = dd.from_pandas(pd, npartitions=3)
    
    #convert to csv file
    df.to_csv('/path/to/data/' + symbol + '-*.csv')  
    return

