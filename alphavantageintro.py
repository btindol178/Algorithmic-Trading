# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:45:34 2021

@author: btindol
"""
import os
print(os.getcwd())  # Prints the current working directory
os.chdir('C:\\Users\\btindol\\OneDrive - Stryker\\Linked In Learn\\Algorithmic Investing\Algorithmic Trading & Quantitative Analysis using Python')  

#####################################################################################################################################################
#imports 
###########################
#!pip install yfinance 
#!pip install pandas 
#!pip install numpy
#!pip install requests
#!pip install datetime
#!pip install yahoofinancials
#!pip install yahoofinancials
#!pip install alpha_vantage 

# ALPHA VANTAGE API KEY 
key = '767CWO9L2SUW1XT9' # Your API Key

# "pip install alpha_vantage" (if you haven't done so)
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import requests
import datetime as dt
import time

###############################################################################
# or key=open(key_path,'r').read(),) # to hide key..
ts = TimeSeries(key=key,output_format='pandas')
data = ts.get_daily(symbol='SYK',outputsize='full')[0] # stryker data
data.columns = ['open','high','low','close','volume']

# extracting stock data(historical for multipl stocks)
# only 5 tickers at once ... 
all_tickers =  ['AMZN','MSFT','INCT','GOOG','INFY.NS']
close_prices = pd.DataFrame()
ticker =  ['AMZN']
for ticker in all_tickers:
    ts=TimeSeries(key=key,output_format='pandas')
    data = ts.get_intraday(symbol=ticker,interval='1min',outputsize='compact')[0]
    data.columns = ['open','high','low','close','volume']
    close_prices[ticker] =data['close']                                                                        
    
    
# get around the 5 limitation
all_tickers =  ['AMZN','MSFT','INCT','GOOG','INFY.NS','SYK']
close_prices = pd.DataFrame()
api_call_count = 0
ticker =  ['AMZN']
for ticker in all_tickers:
    start_time = time.time() 
    ts=TimeSeries(key=key,output_format='pandas')
    data = ts.get_intraday(symbol=ticker,interval='1min',outputsize='compact')[0]
    api_call_count += 1 
    data.columns = ['open','high','low','close','volume']
    close_prices[ticker] = data['close'] 
    if api_call_count ==5:
        api_call_count = 0
        time.sleep(60 - time.time()) 
        
close_prices = pd.DataFrame()
data['close']