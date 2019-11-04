import plotly.graph_objects as go
import pandas as pd
import plotly

df = pd.read_csv("MSFT2014-18.csv")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.Date, y=df['High'], name="MSFT High",
                         line_color='royalblue'))

fig.add_trace(go.Scatter(x=df.Date, y=df['Low'], name="MSFT Low",
                         line_color='red'))

fig.update_layout(title_text='Microsoft Stock Price Over Time',
                  yaxis_title='Price (USD)',
                  xaxis_rangeslider_visible=True)

plotly.offline.plot(fig, filename='timeserise_plotlygo_msft_stock.html')
