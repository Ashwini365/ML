import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, np.nan, 40, 35, 45],
    'Salary': [50000, 60000, np.nan, 55000, 65000]
})
print(f"Original DataFrame:\n{df}")

# Mean imputation
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(f"\nDataFrame after Mean Imputation:\n{df}")

# Median imputation
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
print(f"\nDataFrame after Median Imputation:\n{df}")
