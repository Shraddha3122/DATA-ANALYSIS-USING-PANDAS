# Merge two DataFrames, df1 and df2, on a common column called ID

import pandas as pd

# Sample DataFrame 1
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}

# Sample DataFrame 2
data2 = {
    'ID': [3, 4, 5, 6],
    'Score': [88, 92, 75, 85],
    'Grade': ['A', 'A', 'B', 'B']
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Display the original DataFrames
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Merge the DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Display the merged DataFrame
print("\nMerged DataFrame:")
print(merged_df)