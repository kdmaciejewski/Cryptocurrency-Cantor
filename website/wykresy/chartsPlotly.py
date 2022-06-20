from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px

cryptocurrencies = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'BNB-USD']

df = yf.download(cryptocurrencies, start='2020-01-01',
                 end=datetime.today().strftime('%Y-%m-%d'))
df.isnull().any()
adj_close = df['Adj Close']
print(adj_close.head())

# def all_charts():
#     adj_close.plot(grid=True, figsize=(15, 10))
#     plt.show()
    # fig = px.line(adj_close, y="BTC-USD")
    # fig.show()

def bitcoin():
    fig = px.line(adj_close, y="BTC-USD")
    fig.show()

def etherium():
    # adj_close['ETH-USD'].plot(grid=True, figsize=(15, 10))
    # plt.show()
    fig = px.line(adj_close, y="ETH-USD")
    fig.show()

def dogecoin():
    fig = px.line(adj_close, y="DOGE-USD")
    fig.show()

def binance():
    fig = px.line(adj_close, y="BNB-USD")
    fig.show()


if __name__ == '__main__':

    #all_charts()
    bitcoin()
    etherium()
    dogecoin()
    binance()



