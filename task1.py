import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


full_df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_1019308.csv', skiprows=4)
metadata_df = pd.read_csv('Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_1019308.csv')


true_countries_df = metadata_df[metadata_df['Region'].notna()]


countries_only_df = full_df[full_df['Country Code'].isin(true_countries_df['Country Code'])]


top_5_df = countries_only_df.sort_values(by='2024', ascending=False).head(5)


print("--- Correct Top 5 Most Populous Countries in 2024 ---")
print(top_5_df[['Country Name', '2024']])



sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))

sns.barplot(
    x='Country Name',
    y='2024',
    data=top_5_df,
    palette='plasma'
)

plt.xticks(rotation=45, ha='right')


plt.title('Top 5 Most Populous Countries (2024)', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Total Population (in billions)', fontsize=12)


plt.tight_layout()


plt.savefig('top_5_population_corrected_chart.png')
print("\nCorrected bar chart saved as 'top_5_population_corrected_chart.png'")