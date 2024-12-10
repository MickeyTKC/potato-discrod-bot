import pandas as pd
import pandas_ta as ta
from datetime import date

#Config
sectors = ["XLK", "XLC", "XLF", "XLU", "XLP", "XLV", "XLE", "XLI", "XLY"]
sectors_name = {
    'XLK': 'Technology',
    'XLC': 'Communication Services',
    'XLF': 'Financial',
    'XLU': 'Utilities',
    'XLP': 'Consumer Staples',
    'XLV': 'Health Care',
    'XLE': 'Energy',
    'XLI': 'Industrials',
    'XLY': 'Consumer Discretionary'
}

#Read File
file_path = "sectors.png"
data = pd.read_csv("data/sectors.csv")
report = {}

def create():
    #Looping sector
    for sector in sectors:
        #Get Sector Data
        report[sector] = data[data['Ticker'] == sector]
        #Convert Date to Datetime
        report[sector]['Date'] = pd.to_datetime(report[sector]['Date'], format='%Y-%m-%d')
        #Only 1 Year Data
        report[sector] = report[sector][report[sector]['Date'] >= date.today() - pd.DateOffset(years=1)]
        #RSI by close
        report[sector]['RSI'] = ta.rsi(report[sector]['Close'], length=14)

    import numpy as np
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(3, 3, figsize=(7,7), layout='constrained')

    for col in range(3):
        for row in range(3):
            sector = sectors[col + row * 3]
            axs[row, col].plot(report[sector]['Date'], report[sector]['Close'], label='Price')
            axs[row, col].set_title(f"{sector}-{sectors_name[sector]}")
            axs[row, col].legend()
            #date x-axis font size smaller
            axs[row, col].set_xticklabels(axs[row, col].get_xticklabels(), rotation=45, ha='right', fontsize=8)

    plt.savefig(file_path, dpi=600)