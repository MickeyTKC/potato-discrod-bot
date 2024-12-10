import pandas as pd
import pandas_ta
import numpy as np
from datetime import date

debug = True
source = "strategies\sp500_breadth\sp500.csv"
file_path = "market_breadth.png"

def create():
    #Read File
    data = pd.read_csv(source)
    #Convert Date to datetime
    data['Date'] = pd.to_datetime(data['Date'])
    #Get distinct Tickers
    tickers = data['Ticker'].unique()
    data = data.set_index(['Date','Ticker'])
    #SMA with 20, 50 ,200 with all tickers
    data['20_ma'] = data.groupby(level=1)['Adj Close'].transform(lambda x: pandas_ta.sma(close=x, length=20))
    data['50_ma'] = data.groupby(level=1)['Adj Close'].transform(lambda x: pandas_ta.sma(close=x, length=50))
    data['200_ma'] = data.groupby(level=1)['Adj Close'].transform(lambda x: pandas_ta.sma(close=x, length=200))
    #Above or Below MA
    data['above_20_ma'] = data.apply(lambda x: 1 if (x['Adj Close'] > x['20_ma']) else 0, axis=1)
    data['above_50_ma'] = data.apply(lambda x: 1 if (x['Adj Close'] > x['50_ma']) else 0, axis=1)
    data['above_200_ma'] = data.apply(lambda x: 1 if (x['Adj Close'] > x['200_ma']) else 0, axis=1)
    if debug == True:
        print(data)
    #Plot 
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    #Lines for above 20, above 50, above 200
    ax_20 = ((data.groupby(level=0)['above_20_ma'].sum()/len(tickers))*100).plot(figsize=(16,6), color='green')
    ax_50 = ((data.groupby(level=0)['above_50_ma'].sum()/len(tickers))*100).plot(figsize=(16,6), color='blue')
    ax_200 = ((data.groupby(level=0)['above_200_ma'].sum()/len(tickers))*100).plot(figsize=(16,6), color='red')
    #Line for axis 20, 80
    ax_20.axhline(y=20, color='green', linestyle='--')
    ax_20.axhline(y=80, color='red', linestyle='--')
    #Setting up the axis
    ax_50.yaxis.set_label_position("right")
    ax_50.yaxis.tick_right()
    ax_50.set_ylabel('Percentile')
    #Title
    plt.title('SPX Stocks Above Moving Average')
    plt.savefig(file_path, dpi=600)
    if debug == True:
        plt.show()
    #save as image
    

if debug == True:
    create()