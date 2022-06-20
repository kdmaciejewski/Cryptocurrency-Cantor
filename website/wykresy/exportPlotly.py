import plotly.express as px
from datetime import datetime
import yfinance as yf

if __name__ == '__main__':
    cryptocurrencies = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'BNB-USD']

    df = yf.download(cryptocurrencies, start='2020-01-01',
                     end=datetime.today().strftime('%Y-%m-%d'))
    df.isnull().any()
    adj_close = df['Adj Close']
    fig = px.line(adj_close, y="BTC-USD")
    fig.write_html("plot-btc.html")
    fig = px.line(adj_close, y="ETH-USD")
    fig.write_html("plot-eth.html")
    fig = px.line(adj_close, y="DOGE-USD")
    fig.write_html("plot-doge.html")
    fig = px.line(adj_close, y="BNB-USD")
    fig.write_html("plot-bnb.html")