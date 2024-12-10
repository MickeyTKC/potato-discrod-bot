from datetime import date
import requests
import yfinance as yf
import pandas as pd

#config
start_date = date.today() - pd.DateOffset(years=5)
file_path = "data/spx500.csv"

#get Ticker List
def get_tickers() -> pd.DataFrame:
    # Ref: https://stackoverflow.com/a/75845569/
    url = 'https://www.slickcharts.com/sp500'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'  # Default user-agent fails.
    response = requests.get(url, headers={'User-Agent': user_agent})
    return pd.read_html(response.text, match='Symbol', index_col='Symbol')[0]

def fetch_data():
    #Get Tickers
    tickers = get_tickers().index.tolist()
    tickers = [ticker.replace('.', '-') for ticker in tickers]

    #Download Data
    data = yf.download(tickers, start=start_date, end=date.today())
    data = data.stack()
    data.to_csv(file_path)