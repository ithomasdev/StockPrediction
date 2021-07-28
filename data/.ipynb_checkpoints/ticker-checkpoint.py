import yfinance as yf
import pandas as pd
import dask.dataframe as dd
from pandas_datareader import data as pdr
from dask.dataframe import from_pandas
from os.path import expanduser

# get dataframe using folder and stock name
# takes csv file and reads + returns the dataframe
def get_dataframe(symbol):
    return pd.read_csv(symbol)

# create excel file using dask and yfinance
# needs to have a time interval set by default
# timeStart and timeEnd are for dates
def create_excel(symbol, timeStart, timeEnd):

    #get dataframe for pandas
    pd = pdr.get_data_yahoo(symbol, start=timeStart, end=timeEnd)
    
    print (pd)
    
    #convert from pandas to dask dataframe
    df = dd.from_pandas(pd, npartitions=3)
    
    #make filepath
    home = expanduser("~")
    
    filename = "\Desktop\\" + symbol + " " + timeStart + " to " + timeEnd
    
    filepath = home + filename + ".csv"
    
    print ("Created in: " + filepath)
    
    #convert to csv file
    df.to_csv(filepath, single_file = True)
    return