import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- DATA CLEANING AND PREPARATION ---

# Step 1: Load both the main data and the country metadata
full_df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_1019308.csv', skiprows=4)
metadata_df = pd.read_csv('Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_1019308.csv')

# Step 2: Filter out the aggregate regions to get a list of only true countries
# The aggregate regions (like 'World') do not have a 'Region' listed in the metadata.
# We will select only the rows where the 'Region' column is not empty.
true_countries_df = metadata_df[metadata_df['Region'].notna()]

# Step 3: Filter the main population DataFrame to keep only the true countries
# We use .isin() to check if the 'Country Code' from our main data exists in our clean list of countries.
countries_only_df = full_df[full_df['Country Code'].isin(true_countries_df['Country Code'])]

# Step 4: NOW find the top 5 most populous countries from the clean data
top_5_df = countries_only_df.sort_values(by='2024', ascending=False).head(5)

# Optional: Print the new, correct top 5 to the terminal
print("--- Correct Top 5 Most Populous Countries in 2024 ---")
print(top_5_df[['Country Name', '2024']])


# --- PLOTTING ---

# Step 5: Set the plot style and create the figure
sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))

# Step 6: Create the vertical bar chart with the corrected data
sns.barplot(
    x='Country Name',
    y='2024',
    data=top_5_df,
    palette='plasma'
)

# Step 7: Rotate the x-axis labels
plt.xticks(rotation=45, ha='right')

# Step 8: Add title and labels
plt.title('Top 5 Most Populous Countries (2024)', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Total Population (in billions)', fontsize=12)

# Step 9: Ensure plot layout is tight
plt.tight_layout()

# Step 10: Save the plot
plt.savefig('top_5_population_corrected_chart.png')
print("\nCorrected bar chart saved as 'top_5_population_corrected_chart.png'")