import pandas as pd
import matplotlib.pyplot as plt

# Apple stock price data for 2014-2019
# Data were collected from https://finance.yahoo.com/quote/AAPL/history?p=AAPL

# TODO: Generate Data for plotting
# Load the data from file
apple = pd.read_csv("/datasets/stock/AAPL.csv")
print(apple.head())

# Check if there is any row with empty value
print(apple.isnull().sum())

# Convert 'Date' column into datetime object format
apple['Date'] = pd.to_datetime(apple['Date'])

# Set datetime object as index of the DataFrame to explore the data
apple = apple.set_index('Date')
print(apple.head())

# TODO: Generate the plot
# cols_plot = ['High', 'Low']
# apple.loc['2019', cols_plot].plot()
#
# # TODO: Add x_label and y_label
# plt.xlabel('Year-Month')
# plt.ylabel('Apple Stock Price')


# 1) RGB tuple:
# fig, ax = plt.subplots(facecolor=(.18, .31, .31))
# # 2) hex string:
# ax.set_facecolor('#eafff5')
# # 3) gray level string:
# ax.set_title('Voltage vs. time chart', color='0.7')
# # 4) single letter color string
# ax.set_xlabel('time (s)', color='c')
# # 5) a named color:
# ax.set_ylabel('voltage (mV)', color='peachpuff')
# # 6) a named xkcd color:
# ax.plot(t, s, 'xkcd:crimson')
# # 7) Cn notation:
# ax.plot(t, .7*s, color='C4', linestyle='--')
# # 8) tab notation:
# ax.tick_params(labelcolor='tab:orange')
#
plt.legend()
plt.show()
