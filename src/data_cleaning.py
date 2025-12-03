import pandas as pd
 
def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)


# Display the first few rows of the DataFrame
print(df.head())

# Standardize column names to lowercase remove whitespace and replace spaces with underscores
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

#fill spaces or double spaces in price and qty columns with a zero
df['price'] = df['price'].replace(' ', 0).replace('  ', 0).astype(float)
df['qty'] = df['qty'].replace(' ', 0).replace('  ', 0).astype(int)


# Handle missing values by filling them with appropriate defaults for columns prodname, price, qty, and date_sold
df['prodname'] = df['prodname'].fillna('Unknown Product')
df['price'] = df['price'].fillna(0)
df['qty'] = df['qty'].fillna(0)
df['date_sold'] = pd.to_datetime(df['date_sold'], errors='coerce')
df['date_sold'] = df['date_sold'].fillna(pd.Timestamp('2024-01-01'))

#remove negitive values in price and qty columns by converting them to absolute values
df['price'] = df['price'].abs()
df['qty'] = df['qty'].abs()

#Strip leading and trailing whitespace from all the data under prodname and category columns remove the quotation marks if any
df['prodname'] = df['prodname'].str.strip().str.replace('"', '')
df['category'] = df['category'].str.replace('"', '').str.strip()
df['category'] = df['category'].str.strip()

#lowecase all the data under category and prodname columns
df['prodname'] = df['prodname'].str.lower()
df['category'] = df['category'].str.lower()

#remove double spaces in prodname and category columns
df['prodname'] = df['prodname'].str.replace('  ', ' ')
df['category'] = df['category'].str.replace('  ', ' ')


# Remove duplicates
df = df.drop_duplicates()

# Show the new cleaned DataFrame
print("-" * 100)
print(df)
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())