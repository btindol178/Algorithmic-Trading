# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:12:34 2021

@author: btindol
"""

import os
print(os.getcwd())  # Prints the current working directory
os.chdir('C:\\Users\\btindol\\OneDrive - Stryker\\Linked In Learn\\Algorithmic Investing\Algorithmic Trading & Quantitative Analysis using Python')  

#####################################################################################################################################################
#imports 
#!pip install yfinance 
#!pip install pandas 
#!pip install numpy
#!pip install requests
#!pip install datetime
#!pip install yahoofinancials

#!pip install yahoofinancials
from yahoofinancials import YahooFinancials

import pandas as pd
import numpy as np
import requests
import datetime as dt

##############################
yahoo_financials = YahooFinancials(ticker)
data = yahoo_financials.get_historical_price_data("2018-01-01","2020-01-01","daily")

# get multiple tickers yahoo financials wants dates to be in string
all_tickers =  ['AMZN','MSFT','INCT','GOOG','INFY.NS','SYK']
close_prices = pd.DataFrame()
end_date = (dt.date.today()).strftime('%Y-%m-%d')
beg_date = (dt.date.today()-dt.timedelta(1825)).strftime('%Y-%m-%d')
for ticker in all_tickers:
    yahoo_financials = YahooFinancials(ticker)
    json_obj = yahoo_financials.get_historical_price_data(beg_date,end_date,"daily")
    ohlv = json_obj[ticker]['prices']
    temp = pd.DataFrame(ohlv)[["formatted_date","adjclose"]] # convert list of dictionaries into dataframe  just look at this pd.DataFrame(ohlv)
    temp.set_index("formatted_date",inplace=True) # make formatted date the index (best practice to have date in index for time series data)
    temp.dropna(inplace=True) # because dividend data might hapen and it creates NAN so remove this 
    close_prices[ticker]=temp["adjclose"]