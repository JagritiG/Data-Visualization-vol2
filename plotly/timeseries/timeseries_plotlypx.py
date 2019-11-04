# Using plotly.express
import plotly.express as px
import pandas as pd

df = pd.read_csv('MSFT2014-18.csv')

fig = px.line(df, x='Date', y='High')
fig.show()
