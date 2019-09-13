# Grayscale style sheet
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('grayscale')

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()
ax.set_title('grayscale style sheet')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.plot(x, x, label='linear', linestyle=':', lw=2)
ax.plot(x, x**2, label='quadratic', ls='--', lw=2)
ax.plot(x, x**3, label='cubic', ls='-.', lw=2)


plt.legend()

plt.savefig('grayscale_style_sheet.pdf')
plt.show()
