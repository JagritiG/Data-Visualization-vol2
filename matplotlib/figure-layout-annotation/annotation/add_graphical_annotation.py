# text annotation example
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()
ax.set_title('text annotation')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.plot(x, x, label='linear', linestyle=':')
ax.plot(x, x**2, label='quadratic', ls='--')
ax.plot(x, x**3, label='cubic', ls='-.')

# Annotate with text and arrow
ax.annotate('linear', xy=(0.50, 0.5), xytext=(0.25, 1.5), fontsize=10, fontweight='semibold',
            arrowprops=dict(facecolor='r', arrowstyle='simple'),
            horizontalalignment='right', verticalalignment='top')

ax.annotate('cubic', xy=(1.78, 5.5), xytext=(1.5, 6), fontsize=10, fontweight='semibold',
            arrowprops=dict(facecolor='r', arrowstyle='simple'),
            horizontalalignment='right', verticalalignment='top')

ax.annotate('quadratic', xy=(1.5, 2.2), xytext=(1, 3), fontsize=10, fontweight='semibold',
            arrowprops=dict(facecolor='r', arrowstyle='simple'),
            horizontalalignment='right', verticalalignment='top')

plt.legend()

plt.savefig('graphical_annotation.pdf')
plt.show()

