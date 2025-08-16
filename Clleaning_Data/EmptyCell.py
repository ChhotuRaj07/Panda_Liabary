import pandas as pd

# Read CSV
df = pd.read_csv("data1_cleaned.csv")

# Drop rows with NaN values
df.dropna(inplace=True)

# Save cleaned data back to CSV (overwrite or new file)
df.to_csv("data1_cleaned.csv", index=False)   # creates new file
# OR overwrite original:
# df.to_csv("data1.csv", index=False)

print("NaN values removed and file saved successfully!")
