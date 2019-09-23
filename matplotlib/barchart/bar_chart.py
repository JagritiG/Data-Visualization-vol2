# Plot simple barchart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


plt.style.use('bmh')

# Prepare mock data
organization = ('Microsoft', 'Apple Inc.', 'Alphabet Inc', 'Facebook', 'Intel', 'NVIDIA')
y_pos = np.arange(len(organization))
market_cap = [1050.00, 1008.00, 866.543, 534.843, 234.834, 112.925]


# Plot barchart
def billions(x, pos):
    """The two args are the value and tick position"""
    return '%1.0fB' % (x*1)


formatter = FuncFormatter(billions)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
plt.bar(y_pos, market_cap, align='center', alpha=0.5)
plt.xticks(y_pos, organization, horizontalalignment='right', rotation=25)
plt.ylim(ymin=0)
plt.ylabel('Market Cap')
plt.title('Market Cap 2019')

plt.tight_layout()
plt.savefig('bar_chart.pdf')
plt.show()




