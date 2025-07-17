import pandas as pd

# Load the data
file_path = "../data/sample.csv"  # Adjust path if needed
try:
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully!\n")
except FileNotFoundError:
    print("❌ CSV file not found. Please check the path.")

# Show first few rows
print("🔍 First 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\n🧼 Checking for missing values:")
print(df.isnull().sum())

# Basic statistics
print("\n📊 Summary statistics:")
print(df.describe())

# Optional: Save cleaned data
cleaned_file_path = "../data/cleaned_sample.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\n✅ Cleaned data saved to: {cleaned_file_path}")
