# import pandas as pd
# import numpy as np
# from sklearn.impute import SimpleImputer
#
# # Create a sample DataFrame with missing values
# df = pd.DataFrame({
#     'Numerical_Feature': [10, 20, np.nan, 40, 50],
#     'Categorical_Feature': ['A', 'B', 'A', np.nan, 'C']
# })
#
# print("Original DataFrame:")
# print(df)
#
# # Mean Imputation for Numerical_Feature
# imputer_mean = SimpleImputer(strategy='mean')
# df['Numerical_Feature'] = imputer_mean.fit_transform(df[['Numerical_Feature']])
#
# # Mode Imputation for Categorical_Feature
# imputer_mode = SimpleImputer(strategy='most_frequent')
# df['Categorical_Feature'] = imputer_mode.fit_transform(df[['Categorical_Feature']])
#
# print("\nDataFrame after Mean/Mode Imputation:")
# print(df)
#
#
#
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, np.nan, 40, 35],
    'Salary': [50000, 60000, np.nan, 55000]
})

# Mean imputation
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Median imputation
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print(df)
