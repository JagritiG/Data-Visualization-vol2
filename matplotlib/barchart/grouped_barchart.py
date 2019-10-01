# Grouped barchart
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
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


# Plot Grouped bar between Revenue and Earnings
def billions(x, pos):
    """The two args are the value and tick position"""
    return '$%1.0fB' % (x*1)


formatter = FuncFormatter(billions)
fig, ax = plt.subplots()
bar1 = ax.bar(x - width/2, revenue, width, color='royalblue', label='Revenue')
bar2 = ax.bar(x + width/2, earnings, width, color='mediumseagreen', label='Earnings')


def autolabel(bars):
    """Attach a text label above each bar in *bars*, displaying its height."""
    for rect in bars:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points", ha='center', va='bottom')


autolabel(bar1)
autolabel(bar2)

# Set title, labels, legend
ax.yaxis.set_major_formatter(formatter)
ax.set_title('MSFT - Annual Data\n(2011-2015)', font_param)
ax.set_xticks(x)
ax.set_xticklabels(year)
ax.set_ylim(0, 140)
plt.ylabel('Billions of US $')
ax.legend()
plt.grid(False)

fig.tight_layout()
plt.savefig('grouped_barchart.pdf')
plt.show()

