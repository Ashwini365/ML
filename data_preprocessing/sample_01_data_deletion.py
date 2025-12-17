# import pandas as pd
# import numpy as np
#
# # Sample DataFrame with missing values
# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
#     'Age': [25, 32, np.nan, 45, 28, 35],
#     'Salary': [60000, 45000, 75000, 90000, np.nan, np.nan],
#     'Dept': ['HR', 'Eng', 'Sales', 'Eng', np.nan, 'HR'],
#     'Exp': [2, 8, 4, np.nan, 3, 1]
# })
#
# print("Original Data:\n", df)
#
# # --- 1. Deletion using 'subset' (Targeted Column Deletion) ---
# # Only drop rows where the 'Age' column specifically has a missing value.
# # Rows missing 'Salary' or 'Dept' are kept if 'Age' is present.
# df_subset_cleaned = df.dropna(subset=['Age'])
#
# print("\nData after deleting rows only where 'Age' is missing:\n", df_subset_cleaned)
#
# # --- 2. Deletion using 'thresh' (Minimum Non-Null Threshold) ---
# # Keep only rows that have at least 1 non-NaN values (out of 5 columns).
# df_threshold_cleaned = df.dropna(thresh=1)
#
# print("\nData after deleting rows with fewer than 1 non-NaN values:\n", df_threshold_cleaned)

#
# import pandas as pd
# import numpy as np
#
# # Create a DataFrame with missing values, including one fully empty column
# df = pd.DataFrame({
#     'ID': [1, 2, 3, 4],
#     'Feature_A': [10, 20, np.nan, 40],
#     'Feature_B': [np.nan, np.nan, np.nan, np.nan], # This column is entirely empty
#     'Feature_C': [100, np.nan, 300, 400]
# })
#
# print("Original Data:\n", df)
# print(f"\nShape of original data: {df.shape}")
#
# # --- Deletion using 'thresh=1' on Columns (axis=1) ---
# # Keep columns that have at least 1 non-NaN value (i.e., remove fully empty columns)
# df_threshold_cols_cleaned = df.dropna(axis=1, thresh=1)

# print("\nData after Deletion with thresh=1 on columns (only empty columns removed):\n", df_threshold_cols_cleaned)
# print(f"\nShape of cleaned data: {df_threshold_cols_cleaned.shape}")


import pandas as pd
import numpy as np

# Sample Data (Create your own data here)
df = pd.DataFrame({
    'Metric_1': [10, 20, np.nan, 40, 50],
    'Metric_2': [90, 80, 70, np.nan, 50],
    'Metric_3': [1, np.nan, np.nan, 4, 5],
    'ID': [101, 102, 103, 104, 105]
})

print("Original Data:")
print(df)
print(f"\nOriginal shape: {df.shape}")

# --- The Code to Remove ALL Missing Values (Listwise Deletion) ---
# axis=0 means operate on rows.
# how='any' means drop the row if ANY value within it is NaN.
df_no_missing = df.dropna(axis=0, how='any')

print("\nData after removing ALL rows with missing values:")
print(df_no_missing)
print(f"\nNew shape: {df_no_missing.shape}")
