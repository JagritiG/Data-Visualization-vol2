# Time series plot
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# Apple stock price data for 2014-2015
# Data were collected from https://finance.yahoo.com/quote/AAPL/history?p=AAPL

plt.style.use('seaborn')

# Load the data from file into pandas dataframe
apple = pd.read_csv("AAPL2011-2015.csv")
print(apple.head())

# Check if there is any row with empty value
print(apple.isnull().sum())

# Convert 'Date' column into datetime object format
apple['Date'] = pd.to_datetime(apple['Date'])


# Generate the plot
x = apple['Date']
y = apple['Adj Close']
label = 'Adj Close'


def billions(x, pos):
    """The two args are the value and tick position"""
    return '$%1.0fB' % (x*1)


formatter = FuncFormatter(billions)

fig, ax = plt.subplots(figsize=(10, 5))
ax.yaxis.set_major_formatter(formatter)
ax.plot(x, y, label=label, color='b')
plt.xticks(horizontalalignment='right', rotation=75)
plt.ylabel('Stock Price', size=10, fontweight='semibold')
plt.title('Apple Stock Price', font_param)
plt.ylim(ymin=0)
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()

# Save and show figure
plt.savefig('apple_stock_price.pdf')
plt.show()

