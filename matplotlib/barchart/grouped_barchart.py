# Grouped barchart
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

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
rects1 = ax.bar(x - width/2, revenue, width, label='Revenue')
rects2 = ax.bar(x + width/2, earnings, width, label='Earnings')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.yaxis.set_major_formatter(formatter)
ax.set_title('Microsoft Annual Financial Report')
ax.set_xticks(x)
ax.set_xticklabels(year)
ax.set_ylim(0, 140)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.savefig('grouped_barchart.pdf')
plt.show()

