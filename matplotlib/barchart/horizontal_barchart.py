# Horizontal barchart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# Market Capitalization of different technology industries.
# Data were collected from Yahoo Finance (September 2015)
# https://finance.yahoo.com/screener/predefined/ms_technology

plt.style.use('seaborn-whitegrid')

# Prepare data
organization = ('Microsoft', 'Apple Inc.', 'Alphabet', 'Intel', 'Nvidia')
y = np.arange(len(organization))
market_cap = [334.39, 619.76, 432.15, 132.06, 11.69]


# Plot horizontal bar chart
def billions(x, pos):
    """The two args are the value and tick position"""
    return '%1.0fB' % (x*1)


formatter = FuncFormatter(billions)

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(formatter)
ax.barh(y, width=market_cap, align='center', color='darkorange')
ax.set_yticks(y)
ax.set_yticklabels(organization)
ax.invert_yaxis()  # labels read top-to-bottom
ax.tick_params(width=0)
plt.xlabel('Market Capitalization (Billions of US $)')
plt.title('Market Capitalization 2015', font_param)
plt.grid(False)
plt.tight_layout()

plt.savefig('horizontal_barchart.pdf')
plt.show()

