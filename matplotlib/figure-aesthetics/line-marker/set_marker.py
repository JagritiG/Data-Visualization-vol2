# Set marker style, markersize or ms, markeredgewidth or mew, markeredgecolor or mec,
# markerfacecolor or mfc, markerfacecoloralt or mafcalt, fillstyle ('full', 'left', 'right', 'bottom', 'top', 'none').
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 10)

fig, ax = plt.subplots()
ax.set_title('Simple plot')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.plot(x, x, label='x', c='orange', marker='o', markersize=8, fillstyle='full')
ax.plot(x, 2*x, label='2x', c='C5', marker='d', ms=8, markeredgecolor='C5', fillstyle='top')
ax.plot(x, 3*x, label='3x', c='C7', marker='^', ms=9, mec='C5', mfc='C7', fillstyle='none')


plt.legend()
plt.savefig('set_marker.pdf')
plt.show()

