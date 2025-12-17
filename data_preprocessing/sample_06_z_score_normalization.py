# import numpy as np
# from sklearn.preprocessing import StandardScaler
# import pandas as pd
#
# # Example data: a 2D array (features x samples) or a Pandas DataFrame
# data = np.array([[10.], [20.], [30.], [40.], [50.]])
#
# # Initialize the StandardScaler
# scaler = StandardScaler()
#
# # Fit the scaler to the data and transform the data
# # The result will be a NumPy array
# standardized_data = scaler.fit_transform(data)
#
# print("Original Data:\n", data.flatten())
# print("\nStandardized Data (Scikit-Learn):\n", standardized_data.flatten())

import numpy as np

data = np.array([75, 82, 90, 68, 95])

# Manual calculation using NumPy functions
data_mean = np.mean(data)
data_std = np.std(data)

normalized_data = (data - data_mean) / data_std

print("Original Data:", data)
print("Normalized Data (Z-scores):", normalized_data.round(3))

# Verify the properties of the normalized data
print("\nMean of normalized data:", np.mean(normalized_data).round(5))
print("Std Dev of normalized data:", np.std(normalized_data).round(5))
