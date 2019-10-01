# Line plot of residential electricity usage of san Diego (1990-2014)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# Data is taken from https://data.ca.gov/.
# Source: California Electricity Consumption Database
# Electricity consumption data by county
# All Usage Expressed in Millions of kWh (GWh)

# Prepare data
sd_electricity = pd.read_csv('sd_electricity.csv')
print(sd_electricity.head())
print(sd_electricity.info())


# Plot line graph of San Diego residential electricity usage
fig, ax = plt.subplots()
ax.plot(sd_electricity['Year'],
        sd_electricity['Usage'],
        label='Electricity Usage (GWh)', c='royalblue')

ax.set_xlabel('Year', fontsize=10, fontweight='semibold')
ax.set_ylabel('Electricity Usage (GWh)', fontsize=10, fontweight='semibold')
ax.set_title('San Diego Residential Electricity Usage\n(1990-2014)', font_param, c='b')
ax.grid(color='lightgray', linestyle='--', linewidth='0.5')
plt.xlim(1990, 2015)
plt.legend()
plt.tight_layout()


plt.savefig("lineplot_sd_electricity.pdf")
plt.show()
