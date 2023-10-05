import pandas as pd

# Create a sample dataset with categorical data
data = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Green'],
    'Size': ['Small', 'Large', 'Medium', 'Medium', 'Small'],
    'Category': ['A', 'B', 'A', 'C', 'B']
})

# Display the original dataset
print("Original Dataset:")
print(data)

# Encode categorical data using one-hot encoding
encoded_data = pd.get_dummies(data, columns=['Color', 'Size', 'Category'])

# Display the encoded dataset
print("\nEncoded Dataset (One-Hot Encoding):")
print(encoded_data)
