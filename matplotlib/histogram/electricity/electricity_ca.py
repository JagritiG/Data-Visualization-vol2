import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# Data is taken from https://data.ca.gov/.
# Source: California Electricity Consumption Database
# Electricity consumption data by county
# All Usage Expressed in Millions of kWh (GWh)

plt.style.use('bmh')

# Prepare data
residential_electricity = pd.read_csv('ElectricityByCounty.csv',)
print(residential_electricity.head())
print(residential_electricity.info())

# San Diego electricity consumption
sd_residential_electricity = residential_electricity[residential_electricity['County'] == 'SAN DIEGO']
print(sd_residential_electricity.head())

# Transform wide data into tidy long data using pandas melt() function
sd_residential_electricity_long = pd.melt(sd_residential_electricity,
                                          id_vars=['Total Usage','Sector', 'County'],
                                          var_name='Year',
                                          value_name='Usage')

print(sd_residential_electricity_long.head())

# Create DataFrame with year and Electricity Usage for San Diego
sd_electricity_usage = sd_residential_electricity_long[['Year', 'Usage']]
sd_electricity_usage_sorted = sd_electricity_usage.sort_values('Year')
print(sd_electricity_usage_sorted.head())

# Plot data
num_bins = 5

fig, ax = plt.subplots()

# The histogram of the data
n, bins, patches = ax.hist(sd_electricity_usage_sorted['Usage'], num_bins, density=1)

ax.set_xlabel('Electricity Usage in Millions of kWh (GWh)')
ax.set_title('San Diego Residential Electricity Consumption 1990-2018', font_param)

fig.tight_layout()
plt.savefig('sandiego_electricity_consumption.pdf')
plt.show()
