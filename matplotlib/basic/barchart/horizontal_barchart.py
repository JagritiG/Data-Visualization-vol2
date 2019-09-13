# Plot simple horizontal barchart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


plt.style.use('ggplot')

# Prepare mock Data
organization = ('Microsoft', 'Apple Inc.', 'Alphabet Inc', 'Facebook', 'Intel', 'NVIDIA')
y_pos = np.arange(len(organization))
market_cap = [1050.00, 1008.00, 866.543, 534.843, 234.834, 112.925]


# Plot horizontal barchart
def billions(x, pos):
    """The two args are the value and tick position"""
    return '%1.0fB' % (x*1)


formatter = FuncFormatter(billions)

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(formatter)
ax.barh(y_pos, market_cap, align='center', alpha=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels(organization)
ax.invert_yaxis()  # labels read top-to-bottom
plt.xlabel('Market Cap')
plt.title('Market Cap 2019')

plt.tight_layout()
plt.savefig('horizontal_barchart.pdf')
plt.show()

