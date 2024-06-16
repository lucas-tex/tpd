import pandas as pd

# Replace the path with your actual file path and ensure that the backslashes are escaped or use a raw string
file_path = r"Employee_Salaries.csv"

# Read the CSV file
arquivo_csv = pd.read_csv(file_path, sep=',')

# Check for missing values in each column
missing_values = arquivo_csv.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Check for inconsistent data types
data_types = arquivo_csv.dtypes
print("\nData types of each column:")
print(data_types)

# Display unique data types in the DataFrame
unique_data_types = data_types.unique()
print("\nUnique data types in the DataFrame:")
print(unique_data_types)