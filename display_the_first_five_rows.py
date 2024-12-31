# Load a CSV file named records.csv into a pandas DataFrame and
# display the first five rows.


import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/Assessment/10. DATA ANALYSIS USING PANDAS/records.csv')

# Display the first five rows of the DataFrame
print(df.head())