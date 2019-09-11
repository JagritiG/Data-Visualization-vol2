import pandas as pd
import datetime


# Historical Data of Median Prices of Existing Detached Homes of california
# County Sales & Price Statistics
# https://car.sharefile.com/share/view/s14d6028fcc046b1b

# Load data from file with skipping first 7 rows
df = pd.read_csv("../datasets/cal-housing-price/MedianPricesofExistingDetachedHomesHistoricalData.csv", skiprows=7, header=0)
print(df.head())
# Prepare data
detached_home_price = df[['Year', 'Los Angeles', 'San Diego', 'San Francisco']]
detached_home_price.columns = ['month', 'LosAngeles', 'SanDiego', 'SanFrancisco']

print(detached_home_price.head())
# print(detached_home_price.tail())
# print(detached_home_price.columns)
# print(detached_home_price.info())
# print(detached_home_price.iloc[:5, :10])

# Working with missing data
# Count non-missing values
# print(detached_home_price.count())

# Count missing values
# num_rows = detached_home_price.shape[0]
# print(num_rows)
# num_missing_value = num_rows - detached_home_price.count()
# print(num_missing_value)

# Cleaning missing value
# Replace missing values with the last know value using fill forward method ffill()
detached_home_price = detached_home_price.ffill()
detached_home_price = detached_home_price.bfill()


print(detached_home_price.dtypes)
detached_home_price.isnull().sum()
# Convert "Year" column into datetime format



# Write cleaned data into csv file
# detached_home_price.to_csv('../datasets/cal-housing-price/detachedHomePriceCalifornia.csv')
