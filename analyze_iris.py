import pandas as pd
import sys

# Path to the dataset
file_path = r"c:\Users\HP\Downloads\archive (2)\iris.csv"

try:
    df = pd.read_csv(file_path)
    print(f"Dataset loaded. Shape: {df.shape}")
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nDuplicates:")
    print(f"Number of duplicate rows: {df.duplicated().sum()}")
    
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nBasic Statistics:")
    print(df.describe())
    
    print("\nSpecies Counts:")
    print(df['species'].value_counts())
    
except Exception as e:
    print(f"Error: {e}")
