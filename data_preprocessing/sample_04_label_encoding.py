from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

# 1. Create a sample dataset (a list of colors in this case)
data = ['red', 'blue', 'green', 'red', 'blue', 'red', 'green', 'blue', 'blue', 'green']
df = pd.DataFrame(data, columns=['Color'])

print("Original DataFrame:")
print(df.head())
print("-" * 30)

# 2. Initialize the LabelEncoder
encoder = LabelEncoder()

# 3. Fit and transform the 'Color' column
# This step learns the unique categories and transforms them into integers (e.g., blue=0, green=1, red=2)
df['Encoded_Color'] = encoder.fit_transform(df['Color'])

print("DataFrame after Label Encoding:")
print(df.head())
print("-" * 30)

# 4. View the mapping of original classes to encoded values
print("Mapping of classes (sorted alphabetically by default):")
# The classes_ attribute shows the original labels that were found
for i, item in enumerate(encoder.classes_):
    print(f"{item} -> {i}")
print("-" * 30)

# 5. Inverse transform (convert numerical labels back to original labels)
# This is useful for interpreting predictions
encoded_sample = np.array([2, 0, 1])
original_labels = encoder.inverse_transform(encoded_sample)
print(f"Encoded values: {encoded_sample}")
print(f"Inverse transformed labels: {original_labels}")
