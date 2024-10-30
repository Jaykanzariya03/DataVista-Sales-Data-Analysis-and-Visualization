import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\jayka\Downloads\cust_add.csv")

# Extract the headings (column names)
headings = df.columns.tolist()

# Print the headings
print("Headings:", headings)