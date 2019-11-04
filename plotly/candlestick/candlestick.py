import plotly
import plotly.graph_objects as go
import pandas as pd


msft_stock = pd.read_csv('MSFT2014-18.csv')
print(msft_stock.head())

fig = go.Figure(data=[go.Candlestick(x=msft_stock['Date'],
                open=msft_stock['Open'],
                high=msft_stock['High'],
                low=msft_stock['Low'],
                close=msft_stock['Close'])])


fig.update_layout(
    title='Microsoft stock price for the period:2014-2018',
    yaxis_title='Stock Price (USD)',
)

plotly.offline.plot(fig, filename='candlestick_microsoft_stock.html')
fig.show()



