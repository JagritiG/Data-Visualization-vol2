# Stacked barchart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.style.use('ggplot')

# Prepare data
revenue = [91.15, 96.57, 110.36, 125.84]
earnings = [20.53, 25.48, 16.57, 39.24]
year = [2016, 2017, 2018, 2019]

x = np.arange(len(year))  # the label locations
width = 0.35  # the width of the bars


def billions(x, pos):
    """The two args are the value and tick position"""
    return '$%1.0fB' % (x*1)


formatter = FuncFormatter(billions)
fig, ax = plt.subplots()
p1 = plt.bar(x, revenue, width)
p2 = plt.bar(x, earnings, width, bottom=revenue)

ax.yaxis.set_major_formatter(formatter)
plt.title('Microsoft Annual Financial Report')
plt.xticks(x, year)
plt.ylim(0, 180)
plt.legend((p1[0], p2[0]), ('Revenue', 'Earnings'))

plt.tight_layout()
plt.savefig('stacked_barchart.pdf')
plt.show()

