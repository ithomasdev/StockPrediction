import yfinance as yf
import pandas as pd
import dask.dataframe as dd
import calendar
import os
from pandas_datareader import data as pdr
from dask.dataframe import from_pandas
from os.path import expanduser

# need to create test for this 
# get dataframe using folder and stock name
# takes csv file and reads + returns the dataframe
def get_dataframe(filepath):
    return pd.read_csv(filepath)

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
    filename = symbol + "_" + timeStart + "_to_" + timeEnd
    
    filepath = os.getcwd() + "\\" + symbol + "\\" + filename
    
    print ("Created in: " + filepath)
    
    #convert to csv file
    df.to_csv(filepath, single_file = True)
    return

# creates a large set of data
# timeSpan determines month or year
# duration is the # of years/months you want the data for
# user specifies which month and which year
# NOTE: creating data per year and setting a month, the data created will always start at the given
# --month for every year
def populate_data(symbol, timeSpan, duration, dateYear, dateMonth):

    #gets start and end times for specified time month-by-month
    if 'm' in timeSpan:
        for i in range(duration):
            dates = convert_date(dateYear, dateMonth+i)
            create_excel(symbol, dates[0], dates[1])
            
            
    elif 'y' in timeSpan:
        for i in range(duration):
            for x in range(12):
                #makes sure doesnt go over 12
                if dateMonth+x < 13:
                    dates = convert_date(dateYear+i, dateMonth+x)
                    create_excel(symbol, dates[0], dates[1])

    return

# takes a year and a month
# returns array w/ start and end of that month
def convert_date(year, month):
    
    startDate = ''
    endDate = calendar.monthrange(year, month)[1]
    
    if endDate < 10:
        endDate = "0" + str(date)
    
    if month < 10:
        month = "0" + str(month)
    
    endDate = str(year) + '-' + str(month) + '-' + str(endDate)
    startDate = str(year) + '-' + str(month) + '-' + "01"
    
    dates = [startDate, endDate]
    
    print(dates)
    
    return dates