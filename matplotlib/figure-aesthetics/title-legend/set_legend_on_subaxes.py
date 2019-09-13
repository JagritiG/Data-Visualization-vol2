# Plotting a legend for all the artists on all the sub-axes of a figure.
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2, 10)

fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True)
fig.suptitle('Legend Demo', fontsize=14, fontweight='bold', c='r')
l1, l2 = ax[0].plot(x, x, ':r', x, x**2, '--c')
l3, l4 = ax[1].plot(x, x**3, '-.o', x, np.exp(-x), 's-b')


# Set legend
fig.legend((l1, l2), ('linear','quadratic'), loc='upper left', shadow=True, fancybox=True)
fig.legend((l3, l4), ('cubic', 'exponential'), loc='upper right', shadow=True, fancybox=True)


plt.savefig('set_legend_on_subaxes.pdf')
plt.show()
