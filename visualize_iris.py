import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Paths
input_path = r"d:\ADV_AI\iris_cleaned.csv"
pairplot_out = r"d:\ADV_AI\iris_pairplot.png"
boxplot_out = r"d:\ADV_AI\iris_boxplot.png"

try:
    # Load cleaned data
    print(f"Loading cleaned data from: {input_path}")
    df = pd.read_csv(input_path)
    
    # Set aesthetics
    sns.set_theme(style="whitegrid")
    
    # 1. Pairplot
    print("Generating pairplot...")
    plt.figure(figsize=(10, 8))
    pairplot = sns.pairplot(df, hue="species", palette="viridis", markers=["o", "s", "D"])
    pairplot.savefig(pairplot_out)
    print(f"Pairplot saved to: {pairplot_out}")
    
    # 2. Boxplot
    print("Generating boxplot...")
    plt.figure(figsize=(12, 6))
    melted_df = df.melt(id_vars="species", var_name="Feature", value_name="Measurement")
    boxplot = sns.boxplot(data=melted_df, x="Feature", y="Measurement", hue="species", palette="viridis")
    plt.title("Distribution of Iris Features by Species")
    plt.savefig(boxplot_out)
    print(f"Boxplot saved to: {boxplot_out}")
    
    # Verification
    if os.path.exists(pairplot_out) and os.path.exists(boxplot_out):
        print("Verification: Visualizations created successfully.")
    else:
        print("Verification: One or more visualizations failed to save.")

except Exception as e:
    print(f"Error during visualization: {e}")
