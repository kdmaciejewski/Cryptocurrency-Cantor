import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


if __name__ == '__main__':

    # list of crptocurrencies as ticker arguments
    cryptocurrencies = ['BNB-USD','BTC-USD', 'ETH-USD', 'XRP-USD']

    data = yf.download(cryptocurrencies, start='2020-01-01',
                    end=datetime.today().strftime('%Y-%m-%d'))
    data.head()
    data.isnull().any()
    adj_close=data['Adj Close']
    print(adj_close.head())
    # ploting the adjusted closing price
    fig, axs =plt.subplots(2,2,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
    axs[0,0].plot(adj_close['BNB-USD'])
    axs[0,0].set_title('BNB')
    axs[0,1].plot(adj_close['BTC-USD'])
    axs[0,1].set_title('BTC')
    axs[1,0].plot(adj_close['ETH-USD'])
    axs[1,0].set_title('ETH')
    axs[1,1].plot(adj_close['XRP-USD'])
    axs[1,1].set_title('XRP')
    plt.show()
    # Returns i.e. percentage change in the adjusted close price and drop the first row with NA's
    returns = adj_close.pct_change().dropna(axis=0)
    #view the first 5 rows of the data frame
    returns.head()
    # Cumulative return series
    cum_returns = ((1 + returns).cumprod() - 1) *100
    cum_returns.head()
    cum_returns.plot(figsize=(20,6))
    plt.title('Cumulative Returns')

    plt.show()