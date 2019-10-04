# Stacked Area Graph for residential electricity usage of California county (1990-2014)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('seaborn-whitegrid')

# Data is taken from https://data.ca.gov/.
# Source: California Electricity Consumption Database
# Electricity consumption data by county
# All Usage Expressed in Millions of kWh (GWh)

# ToDo: Prepare data
# Load data from file into panda dataframe
residential_electricity = pd.read_csv('ElectricityByCounty_sdlasf.csv')
print(residential_electricity.head())
print(residential_electricity.info())


# Create 3 DataFrames for San Diego, San Francisco, and Los Angeles
sd_electricity_usage = residential_electricity[residential_electricity['County'] == 'SAN DIEGO']
sf_electricity_usage = residential_electricity[residential_electricity['County'] == 'SAN FRANCISCO']
la_electricity_usage = residential_electricity[residential_electricity['County'] == 'LOS ANGELES']


# Plot Stacked Area Graph
x = sd_electricity_usage['Year']
y = [sd_electricity_usage['Usage'],
     sf_electricity_usage['Usage'],
     la_electricity_usage['Usage']]
labels = ['SAN DIEGO', 'SAN FRANCISCO', 'LOS ANGELES']

fig, ax = plt.subplots()
ax.stackplot(x, y, labels=labels)
ax.legend(loc='upper left')

ax.set_xlabel('Year', fontsize=10)
ax.set_ylabel('Electricity Usage (GWh)', fontsize=10)
ax.set_title('Residential Electricity Usage\n(1990-2014)',
             font_param, c='royalblue')

ax.tick_params(axis='x', direction='out', length=2,
               width=0.5, )
ax.tick_params(axis='y', direction='out', length=2)


plt.grid(False)
plt.tight_layout()
plt.savefig('stacked_plot_residential_electricity_usage.pdf')
plt.show()
