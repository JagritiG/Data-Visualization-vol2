# Histogram of LA International Airport Passenger Count by Carrier Type
import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('ggplot')

# Prepare data
la_airport = pd.read_csv('Los_Angeles_International_Airport_-_Passenger_Count_By_Carrier_Type.csv',)
print(la_airport.head())
print(la_airport.info())

# # Convert 'DataExtractDate' column into datetime object format
# apple['DataExtractDate'] = pd.to_datetime(apple['Date'])
#
# # Set datetime object as index of the DataFrame to explore the data
# apple = apple.set_index('Date')
# print(apple.head())

# Find out unique DataExtractDate for Domestic and International flights
print(la_airport['DataExtractDate'].unique())
print(la_airport['DataExtractDate'].unique())

# Find out unique Domestic and International flight
print(la_airport['Domestic_International'].unique())

# Find out no of rows for Domestic and International flights
print(la_airport.groupby('Domestic_International').size())

# Find out unique flight type for Domestic and International flights
print(la_airport['FlightType'].unique())

# Find out no of rows for each flight type
print(la_airport.groupby('FlightType').size())

# Create 2 DataFrame for Arrival and Departure
arrival = la_airport[la_airport['Arrival_Departure'] == 'Arrival']
departure = la_airport[la_airport['Arrival_Departure'] == 'Departure']

print(arrival.describe())
print(departure.describe())

# Create 2 DataFrame for Domestic and International flight
domestic_arr = arrival[arrival['Domestic_International'] == 'Domestic']
domestic_dep = departure[departure['Domestic_International'] == 'Domestic']
international_arr = arrival[arrival['Domestic_International'] == 'International']
international_dep = departure[departure['Domestic_International'] == 'International']

print(domestic_arr.describe())
print(domestic_dep.describe())
print(international_arr.describe())
print(international_dep.describe())

# Create 3 DataFrame for each flight type of Domestic arrival flights
Charter_dom_arr = domestic_arr[domestic_arr['FlightType'] == 'Charter']
Commuter_dom_arr = domestic_arr[domestic_arr['FlightType'] == 'Commuter']
Scheduled_Carriers_dom_arr = domestic_arr[domestic_arr['FlightType'] == 'Scheduled Carriers']

print(Charter_dom_arr.describe())
print(Commuter_dom_arr.describe())
print(Scheduled_Carriers_dom_arr.describe())

print(Charter_dom_arr.head())

# Create 3 DataFrame for each flight type of International arrival flights
Charter_int_arr = international_arr[international_arr['FlightType'] == 'Charter']
Commuter_int_arr = international_arr[international_arr['FlightType'] == 'Commuter']
Scheduled_Carriers_int_arr = international_arr[international_arr['FlightType'] == 'Scheduled Carriers']

print(Charter_int_arr.describe())
print(Commuter_int_arr.describe())
print(Scheduled_Carriers_int_arr.describe())

# Create 3 DataFrame for each flight type of International departure flights
Charter_int_dep = international_dep[international_dep['FlightType'] == 'Charter']
Commuter_int_dep = international_dep[international_dep['FlightType'] == 'Commuter']
Scheduled_Carriers_int_dep = international_dep[international_dep['FlightType'] == 'Scheduled Carriers']

# Plot data
num_bins = 25

# The histogram of International arrival and departure passenger count for each flight type
fig,ax=plt.subplots(1, 3, figsize=(12, 5))
n, bins, patches = ax[0].hist(Charter_int_arr['Passenger_Count'], num_bins, alpha=0.8, label='arrival', density=True)
n, bins, patches = ax[0].hist(Charter_int_dep['Passenger_Count'], num_bins, alpha=0.8, label='departure', density=True)
n, bins, patches = ax[1].hist(Commuter_int_arr['Passenger_Count'], num_bins, alpha=0.8, label='arrival', density=True)
n, bins, patches = ax[1].hist(Commuter_int_dep['Passenger_Count'], num_bins, alpha=0.8, label='departure', density=True)
n, bins, patches = ax[2].hist(Scheduled_Carriers_int_arr['Passenger_Count'], num_bins, alpha=0.8, label='arrival', density=True)
n, bins, patches = ax[2].hist(Scheduled_Carriers_int_dep['Passenger_Count'], num_bins, alpha=0.8, label='departure', density=True)


ax[0].set_title('Charter Passenger', font_param)
ax[1].set_title('Commuter Passenger', font_param)
ax[2].set_title('Scheduled Carriers Passenger', font_param)
ax[0].set_xlabel('Passenger Count')
ax[1].set_xlabel('Passenger Count')
ax[2].set_xlabel('Passenger Count')


ax[0].legend()
ax[1].legend()
ax[2].legend()


plt.tight_layout()
plt.savefig('histogram_LA_international_airport_passenger_count.pdf')
plt.show()
