import pandas as pd

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

# Save panda dataframe to csv file
nba.to_csv('processed_nba.csv')
