# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 09:27:24 2021

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

import pandas as pd
import numpy as np
import requests
import datetime as dt
import time
from bs4 import BeautifulSoup


# get balance sheet information
url = "https://finance.yahoo.com/quote/MSFT/balance-sheet?p=MSFT"
page = requests.get(url) # get page url with requests
page_content = page.content #page content html
soup = BeautifulSoup(page_content,'html.parser') # make beautiful soup object
tabl = soup.find_all("div",{'class','Pos(r)'}) # doesnt work its not a table right now its dives with subsetable divs 

# Loop through the table if it was a table..
for t in tabl:
    #print(type(t))
    rows = t.find_all("tr")
    for row in rows:
        print(row.get_text())
    

# Get data for a number of stocks and store it int a pandas dataframe
tickers  =['AAPL','MSFT']
financial_dir = {}

for ticker in tickers:
    # getting balance sheet data
    temp_dir = {}
    url = 'https://finance.yahoo.com/quote/' +ticker+'/balance-sheet?p=' +ticker
    page = requests.get(url)
    
