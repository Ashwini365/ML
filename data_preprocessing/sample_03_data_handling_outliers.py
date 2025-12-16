import pandas as pd
import numpy as np

# Example DataFrame with outliers
data = {
    'Feature_A': [10, 20, 30, 40, 50, 60, 70, 80, 90, 1000] # 1000 is an outlier
}
df = pd.DataFrame(data)

# 1. Detect Outliers using the IQR method
Q1 = df['Feature_A'].quantile(0.25) # 25th percentile
Q3 = df['Feature_A'].quantile(0.75) # 75th percentile
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create a boolean mask to identify outliers
outlier_mask = (df['Feature_A'] < lower_bound) | (df['Feature_A'] > upper_bound)
# Calculate the median of non-outlier data
median_value = df.loc[~outlier_mask, 'Feature_A'].median()

# Replace outliers with the calculated median value
df_median_imputed = df.copy()
df_median_imputed.loc[outlier_mask, 'Feature_A'] = median_value

print("Original Data:")
print(df)
print("\nData after Median Imputation:")
print(df_median_imputed)

# Capping and flooring using numpy.clip
df_capped = df.copy()
df_capped['Feature_A'] = np.clip(df_capped['Feature_A'], lower_bound, upper_bound)

print("\nData after Capping/Flooring:")
print(df_capped)

# Filter out rows containing outliers
df_trimmed = df[~outlier_mask]

print("\nData after Removing Outliers:")
print(df_trimmed)


