import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('seaborn-whitegrid')

# Load nba data from file into pandas DataFrame
nba = pd.read_csv('processed_nba.csv',)

# Plot histogram
fig, ax = plt.subplots()
ax.hist(nba['Weight'], 15, color='royalblue', density=1)

ax.set_title('Weight Distribution of NBA Players', font_param)
ax.set_xlabel('Weight in lb')
ax.set_ylabel('Freguency')
ax.tick_params(axis='both', direction='out',
               length=2, width=0.5, )
plt.grid(False)
fig.tight_layout()

# Save and show figure
plt.savefig('nba_weigth.pdf')
plt.show()

