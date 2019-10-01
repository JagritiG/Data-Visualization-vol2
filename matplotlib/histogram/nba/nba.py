import pandas as pd
import matplotlib.pyplot as plt

font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('seaborn')

# Dataset: nba

# ToDo: Prepare data
# Load nba data from file into pandas DataFrame
nba = pd.read_csv('raw_nba.csv',)
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
num_bins = 10

fig, ax = plt.subplots(2, 2, figsize=(10, 5))

# The histogram of the data
n, bins, patches = ax[0, 0].hist(nba['Age'], num_bins, density=1)
n, bins, patches = ax[0, 1].hist(nba['Height'], num_bins, density=1)
n, bins, patches = ax[1, 0].hist(nba['Weight'], num_bins, density=1)
n, bins, patches = ax[1, 1].hist(nba['Salary'], num_bins, density=1)


ax[0, 1].tick_params(axis='x', direction='out', length=6, width=2, labelrotation=90.00)

ax[0, 0].set_title('Histogram of Age', font_param)
ax[0, 1].set_title('Histogram of Height', font_param)
ax[1, 0].set_title('Histogram of Weight', font_param)
ax[1, 1].set_title('Histogram of Salary', font_param)

ax[0, 0].set_xlabel('Age')
ax[0, 1].set_xlabel('Height in ft-inch')
ax[1, 0].set_xlabel('Weight in lb ')
ax[1, 1].set_xlabel('Salary in US Dollar')

ax[0, 0].set_ylabel('Freguency')
ax[0, 1].set_ylabel('Freguency')
ax[1, 0].set_ylabel('Freguency')
ax[1, 1].set_ylabel('Freguency')

fig.tight_layout()
plt.savefig('nba.pdf')
plt.show()

