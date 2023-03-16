# code produced by ChatGPT
import pandas as pd

# Load the dataset
df = pd.read_pickle("data/chi_Chat_time_series_most_crime_CBGs_06_19.p")

# Change the 'Date' column to type datetime
df['Date'] = pd.to_datetime(df['Date'])

# Drop all records with a 'Date' value less than 2019-03-03
df = df[df['Date'] >= '2019-03-03']

# Drop all columns except the specified columns
df = df[['Date', 'Census Block Group', 'Sanitation/Sewer Issue Average Time Open', 'Street Light Repairs Average Time Open', 'Street Repairs Average Time Open', 'Total Crime']]

# Replace NaN values in the 'Total Crime' column with zeros
df['Total Crime'].fillna(0, inplace=True)

# Replace NaN values in the 'Sanitation/Sewer Issue Average Time Open',
# 'Street Light Repairs Average Time Open', and 'Street Repairs Average Time Open'
# columns within each unique 'Census Block Group'
cbg_values = df['Census Block Group'].unique()
for cbg in cbg_values:
    cbg_df = df[df['Census Block Group'] == cbg]
    cbg_df.interpolate(method='ffill', inplace=True)
    cbg_df.interpolate(method='bfill', inplace=True)
    df[df['Census Block Group'] == cbg] = cbg_df

# Save the updated dataset
df.to_pickle("data/chi_Chat_time_series_most_crime_CBGs_06_19_updated.p")