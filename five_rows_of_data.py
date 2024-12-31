#  Create a pandas DataFrame using a dictionary with keys ID, Score,
# and Grade, and provide five rows of data.

import pandas as pd

# Create a dictionary with data
data = {
    'ID': [1, 2, 3, 4, 5],
    'Score': [85, 92, 78, 90, 88],
    'Grade': ['B', 'A', 'C', 'A', 'B']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
