#  Get summary statistics (mean, median, standard deviation, etc.) for numeric columns in a DataFrame.

import pandas as pd

# Sample DataFrame
data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'YearsAtCompany': [1, 2, 3, 4, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Get summary statistics for numeric columns
summary_statistics = df.describe()

# Display the summary statistics
print("\nSummary Statistics:")
print(summary_statistics)