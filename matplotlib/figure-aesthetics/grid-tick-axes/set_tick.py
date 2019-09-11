# Major and minor tickers
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

# Prepare mock data
# Fixing random state for reproducibility
np.random.seed(10000)

# Make up some data in the interval (0, 1)
# Draw random samples from a normal (Gaussian) distribution.
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# Generate figure
plt.figure()

# Plot a Linear scale
fig, ax = plt.subplots()
ax.plot(x, y, label='Linear')

# Make a plot with major ticks that are multiples of 100 and minor ticks that
# are multiples of 10. Label major ticks with '%d' formatting but don't label minor ticks.
ax.xaxis.grid(color='lightgray', linestyle='--', linewidth='0.5', which='both')
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

# For the minor ticks, use no labels; default NullFormatter.
ax.xaxis.set_minor_locator(MultipleLocator(10))

# Set tick parameters
ax.tick_params(direction='out', length=6, width=2, color='r',
               grid_color='r', grid_alpha=0.5, labelrotation=25.0)

# Set title, xlabel, ylabel, legend
ax.set_title('Linear')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
plt.legend()

# Save and show plot
plt.savefig('set_ticks.pdf')
plt.show()
