# Select all rows where the Age column is greater than 30.


import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Teodosija', 'Sutton', 'Taneli', 'Ravshan', 'Ross', 'Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [26, 32, 25, 31, 28, 22, 35, 30, 40, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000, 60000, 70000, 55000, 75000, 65000]}

df = pd.DataFrame(data)

# Filter rows where Age is greater than 30
filtered_rows = df[df['Age'] > 30]

# Display the filtered rows
print(filtered_rows)
