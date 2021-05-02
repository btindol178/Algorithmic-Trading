# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:31:56 2021

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


import yfinance as yf

import pandas as pd
import numpy as np
import requests
#####################################################################################################################################################
# get microsoft data for last 6 month ohlcv data daily data
data = yf.download("MSFT",period = "6mo")
data

# daily data
data2 = yf.download("MSFT",start = '2017-01-01',end='2020-04-24')
data2

# get data smalle than daily data... 
# has to be in last 60 days.
data3 = yf.download("MSFT",period = '1mo',interval='5m')
data3