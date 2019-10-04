import plotly.graph_objects as go
import pandas as pd


apple_stock = pd.read_csv('AAPL2014-2015.csv')
print(apple_stock.head())

fig = go.Figure(data=[go.Candlestick(x=apple_stock['Date'],
                open=apple_stock['Open'],
                high=apple_stock['High'],
                low=apple_stock['Low'],
                close=apple_stock['Close'])])


fig.update_layout(
    title='Apple Stock Price',
    yaxis_title='AAPL Stock',
)
fig.show()


