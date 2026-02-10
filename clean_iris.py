import pandas as pd
import os

# Paths
input_path = r"c:\Users\HP\Downloads\archive (2)\iris.csv"
output_path = r"d:\ADV_AI\iris_cleaned.csv"

try:
    # Load data
    df = pd.read_csv(input_path)
    original_count = len(df)
    print(f"Original dataset loaded. Rows: {original_count}")

    # Remove duplicates
    df_cleaned = df.drop_duplicates()
    cleaned_count = len(df_cleaned)
    duplicates_removed = original_count - cleaned_count
    
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Cleaned dataset rows: {cleaned_count}")

    # Save cleaned data
    df_cleaned.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to: {output_path}")
    
    # Verification
    if os.path.exists(output_path):
        print("Verification: File created successfully.")
    else:
        print("Verification: File creation failed.")

except Exception as e:
    print(f"Error during cleaning: {e}")
