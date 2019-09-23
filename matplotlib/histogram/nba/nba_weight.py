import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('bmh')

# ToDo: Prepare data
# Load nba data from file into pandas DataFrame
nba = pd.read_csv('nba.csv',)
print(nba.head())
print(nba.info())

# ToDo: Working with missing data
# Count non-missing values
print(nba.count())

# Count missing values
num_rows = nba.shape[0]
print(num_rows)
num_missing_value = num_rows - nba.count()
print(num_missing_value)

# Replace missing values using ffill() and bfill()
nba = nba.ffill()
nba = nba.bfill()

print(nba.count())

# ToDo: Plot data
# The histogram of the data
fig, ax = plt.subplots()

mu = nba['Weight'].mean()
median = np.median(nba['Weight'])
sigma = nba['Weight'].std()
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))

ax.hist(nba['Weight'], 10, density=1)
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper right in axes coords
ax.text(0.70, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

ax.set_title('Histogram of Weight', font_param)
ax.set_xlabel('Weight in lb ')
ax.set_ylabel('Freguency')

fig.tight_layout()
plt.savefig('nba_weigth.pdf')
plt.show()

