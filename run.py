import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('results.csv')

# Data Cleaning and Preprocessing
# Fill NULL values in 'AvgDillardsTransactionValue' with the mean of the column
df['AvgDillardsTransactionValue'] = df['AvgDillardsTransactionValue'].fillna(df['AvgDillardsTransactionValue'].mean())

# Fill NULL values in 'PriceDelta' - impute with 0 or a more sophisticated method if needed
df['PriceDelta'] = df['PriceDelta'].fillna(0)

# Convert 'AvgSamsTransactionValue', 'AvgDillardsTransactionValue', and 'PriceDelta' to numeric
df['AvgSamsTransactionValue'] = pd.to_numeric(df['AvgSamsTransactionValue'], errors='coerce')
df['AvgDillardsTransactionValue'] = pd.to_numeric(df['AvgDillardsTransactionValue'], errors='coerce')
df['PriceDelta'] = pd.to_numeric(df['PriceDelta'], errors='coerce')

# Remove rows where 'AvgSamsTransactionValue' is NaN after conversion
df = df[df['AvgSamsTransactionValue'].notna()]

# Aggregate data by state and GeneralCategory
df_grouped = df.groupby(['State', 'GeneralCategory']).agg(
    AvgSamsTransactionValue=('AvgSamsTransactionValue', 'mean'),
    AvgDillardsTransactionValue=('AvgDillardsTransactionValue', 'mean'),
    PriceDelta=('PriceDelta', 'mean')
).reset_index()

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(18, 12))  # Adjusted figure size: Wider and shorter
fig.suptitle('Transaction Value Analysis by State and Category', fontsize=20)

# --- Plot 1: Average Sams Transaction Value by State and Category ---
df_pivot_sams = df_grouped.pivot(index='State', columns='GeneralCategory', values='AvgSamsTransactionValue')
df_pivot_sams.plot(kind='bar', ax=axes[0], colormap='viridis', rot=45, width=0.8)  # Added rotation and width
axes[0].set_title('Average Sams Transaction Value', fontsize=16)
axes[0].set_ylabel('Transaction Value', fontsize=12)
axes[0].set_xlabel('State', fontsize=12) # add an x label to the axes,
axes[0].legend(title='Category')
axes[0].tick_params(axis='x', labelsize=10)  # Adjust x-axis tick label size


# --- Plot 2: Average Dillards Transaction Value by State and Category ---
df_pivot_dillards = df_grouped.pivot(index='State', columns='GeneralCategory', values='AvgDillardsTransactionValue')
df_pivot_dillards.plot(kind='bar', ax=axes[1], colormap='plasma', rot=45, width=0.8) # Added rotation and width
axes[1].set_title('Average Dillards Transaction Value', fontsize=16)
axes[1].set_ylabel('Transaction Value', fontsize=12)
axes[1].set_xlabel('State', fontsize=12)
axes[1].legend(title='Category')
axes[1].tick_params(axis='x', labelsize=10)  # Adjust x-axis tick label size


# --- Plot 3: Price Delta by State and Category ---
df_pivot_delta = df_grouped.pivot(index='State', columns='GeneralCategory', values='PriceDelta')
df_pivot_delta.plot(kind='bar', ax=axes[2], colormap='magma', rot=45, width=0.8)   # Added rotation and width
axes[2].set_title('Price Delta (Sams - Dillards)', fontsize=16)
axes[2].set_ylabel('Price Delta', fontsize=12)
axes[2].set_xlabel('State', fontsize=12)
axes[2].legend(title='Category')
axes[2].tick_params(axis='x', labelsize=10)  # Adjust x-axis tick label size


# Adjust layout to prevent overlapping of subplots
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) #add a little more space for the suptitle

# Save the plot to a file
plt.savefig('transaction_analysis.png')

# Display the plot
plt.show()