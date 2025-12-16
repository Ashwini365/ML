import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, np.nan, 40, 35, 45],
    'Salary': [50000, 60000, np.nan, 55000, 65000]
})

# Mean imputation
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Median imputation
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print(df)
