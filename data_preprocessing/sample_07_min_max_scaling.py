import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def manual_minmax_scaling(data_list):
    min_val = min(data_list)
    max_val = max(data_list)
    # Avoid division by zero if all values are the same
    if max_val == min_val:
        return [0.0 for _ in data_list]

    scaled_list = [(x - min_val) / (max_val - min_val) for x in data_list]
    return scaled_list


# Example with a single feature list
feature_data = [10, 20, 30, 40]
scaled_feature = manual_minmax_scaling(feature_data)
print("Original Data:", feature_data)
print("Manually scaled single feature:", [round(x, 2) for x in scaled_feature])
print("Scaled Data (0 to 1):", scaled_feature)
