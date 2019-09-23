# Stacked Area Graph for residential electricity usage of California county (1990-2018)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}


# Data is taken from https://data.ca.gov/.
# Source: California Electricity Consumption Database
# Electricity consumption data by county
# All Usage Expressed in Millions of kWh (GWh)

# ToDo: Prepare data
# Load data from file into panda dataframe
residential_electricity = pd.read_csv('ElectricityByCounty.csv',)
print(residential_electricity.head())
print(residential_electricity.info())

# Set 'County' as index column index
residential_electricity.set_index('County', inplace=True, drop=True)
print(residential_electricity)

residential_electricity = residential_electricity.loc[['LOS ANGELES', 'SAN DIEGO', 'SAN FRANCISCO']]
residential_electricity.reset_index(inplace=True)
print(residential_electricity.head())

# Transform wide data into tidy long data using pandas melt() function
residential_electricity_long = pd.melt(residential_electricity,
                                          id_vars=['Total Usage','Sector', 'County'],
                                          var_name='Year',
                                          value_name='Usage')

print(residential_electricity_long.head())
electricity_usage_sorted = residential_electricity_long.sort_values('Year')

# Create 3 DataFrames for San Diego, San Francisco, and Los Angeles
sd_electricity_usage = electricity_usage_sorted[electricity_usage_sorted['County'] == 'SAN DIEGO']
sf_electricity_usage = electricity_usage_sorted[electricity_usage_sorted['County'] == 'SAN FRANCISCO']
la_electricity_usage = electricity_usage_sorted[electricity_usage_sorted['County'] == 'LOS ANGELES']


year = sd_electricity_usage['Year']
usage = [sd_electricity_usage['Usage'], sf_electricity_usage['Usage'], la_electricity_usage['Usage']]
labels = ['SAN DIEGO', 'SAN FRANCISCO', 'LOS ANGELES']

fig, ax = plt.subplots()
ax.stackplot(year, usage, labels=labels)
ax.legend(loc='upper left')

ax.set_xlabel('Year', fontsize=10, c='b', fontweight='semibold')
ax.set_ylabel('Electricity Usage (GWh)', fontsize=10, c='b', fontweight='semibold')
ax.set_title('Residential Electricity Usage', font_param, c='r')

ax.tick_params(axis='x', direction='out', length=3, width=0.5, labelrotation=90.00)
ax.grid(color='lightgray', linestyle=':', linewidth='0.5')

plt.tight_layout()
plt.savefig('stacked_plot_residential_electricity_usage.pdf')
plt.show()
