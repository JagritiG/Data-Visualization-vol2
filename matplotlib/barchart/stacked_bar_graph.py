# Stacked barchart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('seaborn-whitegrid')

# Comparison between Microsoft's Revenue and Earnings (in billions of US Dollars)
# Data were collected from Yahoo Finance (June 2011- June 2015)
# https://finance.yahoo.com/quote/MSFT?p=MSFT

# Prepare data
revenue = [69.94, 73.72, 77.84, 86.83, 93.58]
earnings = [23.15, 16.97, 21.86, 22.07, 12.19]
year = [2011, 2012, 2013, 2014, 2015]

x = np.arange(len(year))  # the label locations
width = 0.35  # the width of the bars


# Plot stacked bar chart for revenue vs earnings
def billions(x, pos):
    """The two args are the value and tick position"""
    return '$%1.0fB' % (x*1)


formatter = FuncFormatter(billions)
fig, ax = plt.subplots()
p1 = plt.bar(x, revenue, width)
p2 = plt.bar(x, earnings, width, bottom=revenue)

ax.yaxis.set_major_formatter(formatter)
plt.title('MSFT - Annual Data\n(2011-2015)', font_param)
plt.xticks(x, year)
plt.ylim(0, 180)
plt.ylabel('Billions of US $')
plt.legend((p1[0], p2[0]), ('Revenue', 'Earnings'))
plt.grid(False)
plt.tight_layout()


plt.savefig('stacked_barchart.pdf')
plt.show()

