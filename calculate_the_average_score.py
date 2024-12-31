# Group the DataFrame by Grade and calculate the average Score for each grade.

import pandas as pd

# Sample data
data = {
    'Student': ['Alia', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Grade': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Score': [85, 78, 92, 65, 88, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Group by 'Grade' and calculate the average 'Score'
average_scores = df.groupby('Grade')['Score'].mean().reset_index()

# Rename the columns for clarity
average_scores.columns = ['Grade', 'Average Score']

# Display the result
print("\nAverage Score by Grade:")
print(average_scores)
