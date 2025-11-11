import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("gs://gallstone_bucket/Zomato-data-.csv")

# Load the dataset
# Display basic information
print("Dataset Shape:", df.shape)
print("\nFirst 15 rows:")
print(df.head(15))
print("\nColumn Names:")
print(df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the data - convert rate to numeric by removing '/5'
df['rate_numeric'] = df['rate'].str.replace('/5', '').astype(float)

# Convert yes/no to boolean
df['has_online_order'] = df['online_order'] == 'Yes'
df['has_book_table'] = df['book_table'] == 'Yes'

print("Data cleaning complete. Unique restaurant types:")
print(df['listed_in(type)'].unique())
print(f"\nTotal restaurants: {len(df)}")
