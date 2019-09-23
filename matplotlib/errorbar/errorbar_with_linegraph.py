# Errorbars with Line Graph
import numpy as np
import matplotlib.pyplot as plt
font_param = {'size': 14, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}


# ToDo: Prepare data
x = np.linspace(0, 5.5, 10)
y = 5*np.exp(-x)
x_err = 0.1
y_err = 0.2

# ToDo: Plot data
# Set lower & upper limits of the error
lower_lim = np.array([0, 1, 1, 0, 1, 0, 1, 0, 1, 0], dtype=bool)
upper_lim = np.array([1, 0, 0, 1, 0, 1, 0, 0, 0, 1], dtype=bool)

fig, ax = plt.subplots(figsize=(8, 5))


# standard error bars
ax.errorbar(x, y + 1.5, xerr=x_err, yerr=y_err, ls='--', label='Standard error bar')

# Plot with upper limits
ax.errorbar(x, y + 3, xerr=x_err, yerr=y_err, ls=':', uplims=upper_lim, label='Error bar with uplim')

# Plot with lower limits
ax.errorbar(x, y + 4.5, xerr=x_err, yerr=y_err, ls='-.', lolims=lower_lim, label='Error bar with lolim')

# Plot with upper and lower limits
ax.errorbar(x, y + 6, xerr=x_err, yerr=y_err, ls='-', uplims=upper_lim, lolims=lower_lim, label='Error bar with both uplim and lolim')

ax.set_xlabel('X-label', size=10, fontweight='semibold')
ax.set_ylabel('Y-label', size=10, fontweight='semibold')
ax.set_title('Line plot with error bars', font_param)
plt.legend()

plt.grid(c='lightblue', ls=':')
plt.tight_layout()
plt.savefig('errorbar_with_linegraph.pdf')
plt.show()
