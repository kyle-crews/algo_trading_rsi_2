import yfinance as yf, pandas as pd, shutil, os, time, glob
import numpy as np
import requests
from get_all_tickers import get_tickers as gt
from statistics import mean

# If you have a list of your own you would like to use just create a new list instead of using this, for example: tickers = ["FB", "AMZN", ...] 
tickers = ["AMZN", "CRM", "AAL", "DAL", "TSLA", "MSFT", "FB", "AAPL"]

# Check that the amount of tickers isn't more than 2000
print("The amount of stocks chosen to observe: " + str(len(tickers)))

# These two lines remove the Stocks folder and then recreate it in order to remove old stocks. Make sure you have created a Stocks Folder the first time you run this.
shutil.rmtree("./Stocks")
os.mkdir("./Stocks")

#  These will do the same thing but for the folder holding the RSI values for each stock.
shutil.rmtree("./RSI")
os.mkdir("./RSI")