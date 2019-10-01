# Pie Chart for residential electricity usage by County (state: California) (2014)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# Data is taken from https://data.ca.gov/.
# Source: California Electricity Consumption Database
# Electricity consumption data by county
# All Usage Expressed in Millions of kWh (GWh)

plt.style.use('seaborn')

# Prepare data
residential_electricity = pd.read_csv('ca_electricitybycounty.csv')
print(residential_electricity.head())
print(residential_electricity.info())

# ca_residential_electricity = residential_electricity(columns=['County', '2014'])


residential_electricity.set_index('County', inplace=True, drop=True)
print(residential_electricity)

residential_electricity_by_county = residential_electricity.loc[['LOS ANGELES','SAN DIEGO', 'SAN FRANCISCO', 'RIVERSIDE', 'ORANGE']]
residential_electricity_by_county.reset_index(inplace=True)
print(residential_electricity_by_county.head())

# Plot Pie Chart
fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} GWh)".format(pct, absolute)


wedges, texts, autotexts = ax.pie(residential_electricity_by_county['2014'],
                                  autopct=lambda pct: func(pct, residential_electricity_by_county['2014']),
                                  textprops=dict(color="w"))

ax.legend(wedges, residential_electricity_by_county['County'],
          title="County",
          fontsize="small",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=9, weight="bold")

ax.set_title('Residential Electricity Usage\nCalifornia 2014', font_param)
plt.tight_layout()

plt.savefig('residential_electricity_usage_by_county.pdf')
plt.show()
