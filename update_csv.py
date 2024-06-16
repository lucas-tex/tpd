import pandas as pd

# Replace the path with your actual file path and ensure that the backslashes are escaped or use a raw string
file_path = r"C:\Users\lucas\Workspace\tpd\Employee_Salaries.csv"

# Read the CSV file
arquivo_csv = pd.read_csv(file_path, sep=',')

# Display the DataFrame
print(arquivo_csv.dtypes)