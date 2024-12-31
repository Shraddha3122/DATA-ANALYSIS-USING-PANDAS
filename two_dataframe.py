#Perform a left join between two DataFrames, employees and departments, where the DepartmentID column exists in both DataFrames.


import pandas as pd

# Sample DataFrame for employees
data_employees = {
    'EmployeeID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'DepartmentID': [101, 102, 101, 103]
}

# Sample DataFrame for departments
data_departments = {
    'DepartmentID': [101, 102, 103, 104],
    'DepartmentName': ['HR', 'Marketing', 'Sales', 'IT']
}

# Create DataFrames
employees = pd.DataFrame(data_employees)
departments = pd.DataFrame(data_departments)

# Display the original DataFrames
print("Employees DataFrame:")
print(employees)
print("\nDepartments DataFrame:")
print(departments)

# Perform a left join on 'DepartmentID'
merged_df = pd.merge(employees, departments, on='DepartmentID', how='left')

# Display the merged DataFrame
print("\nMerged DataFrame (Left Join):")
print(merged_df)