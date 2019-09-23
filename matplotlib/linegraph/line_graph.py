# Line plot for residential electricity usage of san Diego (1990-2018)
import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# Data is taken from https://data.ca.gov/.
# Source: California Electricity Consumption Database
# Electricity consumption data by county
# All Usage Expressed in Millions of kWh (GWh)

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
fig, ax = plt.subplots()
ax.plot(sd_electricity_usage_sorted['Year'], sd_electricity_usage_sorted['Usage'], label='Electricity (GWh)', c='r')

ax.set_xlabel('Year', fontsize=10, fontweight='semibold', c='b')
ax.set_ylabel('Electricity Usage (GWh)', fontsize=10, fontweight='semibold', c='b')
ax.set_title('San Diego Residential Electricity Usage', font_param, c='r')

ax.tick_params(axis='x', direction='out', length=6, width=2, labelrotation=90.00)

ax.grid(color='lightgray', linestyle='--', linewidth='0.5')
plt.legend()
plt.tight_layout()
plt.savefig("lineplot_sd_electricity.pdf")
plt.show()
