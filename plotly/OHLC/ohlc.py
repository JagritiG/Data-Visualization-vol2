import plotly.graph_objects as go
import pandas as pd
import plotly

df = pd.read_csv('MSFT2014-18.csv')

fig = go.Figure(data=go.Ohlc(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close']))

plotly.offline.plot(fig, filename='ohlc_plotlygo_msft_stock.html')
fig.show()
