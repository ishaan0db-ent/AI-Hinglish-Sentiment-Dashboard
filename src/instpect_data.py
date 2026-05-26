import pandas as pd
#Loading the Dataset 
df = pd.read_csv("data/raw/output.csv")

#Inspecting the Dataset
#Show first 5 rows of the dataset
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Column names
print("\nColumns  :")
print(df.columns)

#Missing values
print("\nMissing Values :")
print(df.isnull().sum())

#Label distribution
print("\nLabel Distribution :")
print(df['label'].value_counts())

print("\nUnique Sentiments:")
print(df['sentiment'].unique())