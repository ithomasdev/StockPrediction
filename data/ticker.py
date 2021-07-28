import yfinance as yf
import pandas as pd
import dask.dataframe as dd
from pandas_datareader import data as pdr
from dask.dataframe import from_pandas

# get dataframe using folder and stock name
def get_dataframe(symbol):
    return

# create excel file using dask and yfinance
# needs to have a time interval set by default
# dur is duration for time interval, timeStart and timeEnd are for dates
def create_excel(symbol, timeStart, timeEnd, dur):
    
    #set default dates
    start = pd.to_datetime('2020-01-01')
    end = pd.to_datetime('2020-01-01')
    
    #get dates
    start = pd.to_datetime(timeStart)
    end = pd.to_datetime(timeEnd)

    #get dataframe for pandas
    df = pdr.get_data_yahoo(symbol, Start, End)
    
    #get historical market data (default 1 month)
    #df.history(period="1mo")
    
    #convert to dask dataframe
    ddf = df.from_pandas(df)
    
    #convert to csv file
    ddf.to_csv('/path/to/data/' + symbol + '-*.csv')  
    
    return


