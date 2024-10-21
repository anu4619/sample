import pandas as pd
import numpy as np

# Load a CSV file
file_path = 'your_file.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Assuming the CSV has a column named 'values', we can compute basic statistics:
values = data['values']

# Calculate statistics
mean_value = np.mean(values)
median_value = np.median(values)
std_dev_value = np.std(values)

# Display the results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev_value}")
