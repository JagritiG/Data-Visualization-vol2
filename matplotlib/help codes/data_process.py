import pandas as pd
# Source: Infectious Diseases by County, Year and Sex
# url: https://data.chhs.ca.gov/dataset/infectious-disease/resource/75019f89-b349-4d5e-825d-8b5960fc028c
# Load raw data from file into panda dataFrame
raw_data = pd.read_csv('raw_idb_odp_2001-2018.csv')
print(raw_data.head())
print(raw_data.info())

# Check if there is any row with empty value
print(raw_data.isnull().sum())

# Find out unique disease
print(raw_data['Disease'].unique())

# Find out unique year
print(raw_data['Year'].unique())

# Find out unique county
print(raw_data['County'].unique())

# Create a DataFrame for the year 2018
disease_2014 = raw_data[raw_data['Year'] == 2014]
print(disease_2014.head())
print(disease_2014.info())

# Create a DataFrame with SEX='TOTAL'
disease_total = disease_2014[disease_2014['Sex'] == 'TOTAL']
print(disease_total.head())
print(disease_total.info())

# Find number of rows with empty value
print(disease_total.isnull().sum())

# Create a DataFrame with Disease, County, and Cases  for the year 2018
disease = disease_total[['Disease', 'County', 'Cases']]
print(disease.head())
print(disease.info())

# Create a DataFrame with atleast case = 1
disease_atleast_one_case = disease[disease['Cases'] >= 1]
print(disease_atleast_one_case.head())
print(disease_atleast_one_case.info())

# Select some counties
disease_atleast_one_case.set_index('County', inplace=True, drop=True)
print(disease_atleast_one_case)
disease_countywise = disease_atleast_one_case.loc[['ALAMEDA', 'LOS ANGELES', 'SAN DIEGO', 'SAN FRANCISCO']]

disease_countywise.reset_index(inplace=True)
print(disease_countywise.head())
print(disease_countywise.info())

# Select some disease
disease_countywise.set_index('Disease', inplace=True, drop=True)
print(disease_countywise)
selected_disease = disease_countywise.loc[['Amebiasis', 'Salmonellosis', 'Campylobacteriosis', 'Dengue Virus Infection']]
selected_disease.reset_index(inplace=True)
print(selected_disease.head())
print(selected_disease.info())

# Save DataFrame into csv file
selected_disease.to_csv('selected_disease_countywise_2014.csv')
