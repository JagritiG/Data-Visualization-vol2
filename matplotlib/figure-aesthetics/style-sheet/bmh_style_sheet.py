# Bayesian Methods for Hackers style sheet
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()
ax.set_title('bmh style sheet')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.plot(x, x, label='linear', linestyle=':')
ax.plot(x, x**2, label='quadratic', ls='--')
ax.plot(x, x**3, label='cubic', ls='-.')


plt.legend()

plt.savefig('bmh_style_sheet.pdf')
plt.show()

