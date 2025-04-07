import pandas as pd

# Load the dataset (tab-separated format)
df = pd.read_csv('marketing_campaign.csv', sep='\t')

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Handle missing values - Drop rows with missing 'Income'
df = df.dropna(subset=['Income'])

# 3. Standardize column names: lowercase, strip spaces, replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 4. Standardize text values
df['education'] = df['education'].str.strip().str.title()
df['marital_status'] = df['marital_status'].str.strip().str.title()

# 5. Convert 'dt_customer' to datetime format
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')

# 6. Ensure 'income' is of type float
df['income'] = df['income'].astype(float)

# 7. Save the cleaned dataset to a new file
df.to_csv('marketing_campaign_cleaned.csv', index=False)

print("✅ Data preprocessing complete. Cleaned file saved as 'marketing_campaign_cleaned.csv'.")