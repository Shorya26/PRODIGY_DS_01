# ============================================
# Task 02 - Bar Chart & Histogram Visualization
# Prodigy InfoTech Data Science Internship
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load Dataset
# Replace with your filename if needed
data = pd.read_csv("task1.csv")

print(" Dataset Loaded Successfully!\n")
print(data.head())

# Step 2: Convert from wide format to long format
df_long = data.melt(
    id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
    var_name="Year",
    value_name="Population"
)

# Convert year and population columns to numeric
df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")
df_long["Population"] = pd.to_numeric(df_long["Population"], errors="coerce")

print("\nData converted to long format!")

# Step 3: Drop rows with missing values
df_long.dropna(subset=["Population"], inplace=True)

# Step 4: Take the latest year for simplicity (e.g., 2022 if available)
latest_year = df_long["Year"].max()
latest_data = df_long[df_long["Year"] == latest_year]

print(f"\nShowing data for year: {int(latest_year)}")

# Step 5: Bar Chart — Top 10 Most Populous Countries
top10 = latest_data.nlargest(10, "Population")

plt.figure(figsize=(10,6))
sns.barplot(data=top10, x="Population", y="Country Name", palette="cool")
plt.title(f"Top 10 Most Populous Countries in {int(latest_year)}")
plt.xlabel("Population")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Step 6: Histogram — Distribution of Population
plt.figure(figsize=(8,5))
sns.histplot(latest_data["Population"], bins=30, kde=True, color="skyblue")
plt.title(f"Population Distribution Across All Countries ({int(latest_year)})")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.show()
