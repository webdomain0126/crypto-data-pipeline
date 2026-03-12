import pandas as pd
import sqlite3

# Load processed CSV data
df = pd.read_csv("processed_crypto_data.csv")

# Connect to SQLite database
conn = sqlite3.connect("crypto_prices.db")

# Store data in a table
df.to_sql("crypto_prices", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("Data stored successfully in SQLite database!")