from datetime import date
import requests
import yfinance as yf
import pandas as pd

#config
start_date = date.today() - pd.DateOffset(years=5)
file_path = "data/sectors.csv"

def get_tickers():
    return ["XLK", "XLC", "XLF", "XLU", "XLP", "XLV", "XLE", "XLI", "XLY"]

def fetch_data():
    #Get Tickers
    tickers = get_tickers()

    #Download Data
    data = yf.download(tickers, start=start_date, end=date.today())
    data = data.stack()
    data.to_csv(file_path)