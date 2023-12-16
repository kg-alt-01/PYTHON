#Create a pandas data frame using 2D lists.
import pandas as pd
import numpy as np

# Data columns
data = [['Jiya', 17, 'F', 'Science'], 
        ['Maneet', 15, 'M', 'Math'],
        ['Ranbir', np.nan, 'M', 'English'],
        ['Rabnoor', 19, 'F', 'History'],
        ['Manya', np.nan, 'F', 'Physics'],
        ['John', 20, 'M', 'Chemistry']]

# Create DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'Gender', 'Subject'])

# Print DataFrame
print("DataFrame:")
print(df)
print("\n")

# Summary statistics for numerical columns
print("Summary Statistics:")
print(df.describe())
print("\n")

# Sum of Age column
print("Sum of Age:")
print(df['Age'].sum())
print("\n")

# Fill NaN values with mean of the 'Age' column
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)

# Print DataFrame after filling NaN values
print("Fill NaN in 'Age' with mean:")
print(df)
print("\n")

# Drop rows with NaN values
print("Drop NaN rows:")
print(df.dropna())
print("\n")
