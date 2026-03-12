import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("crypto_prices.db")

# Read data from database table
df = pd.read_sql_query("SELECT * FROM crypto_prices", conn)

# Close database connection
conn.close()

# Print data to terminal
print("Crypto Data from Database:")
print(df)

# Create bar chart
plt.figure(figsize=(8,5))
plt.bar(df["coin"], df["price_usd"])

# Chart labels
plt.title("Cryptocurrency Prices")
plt.xlabel("Cryptocurrency")
plt.ylabel("Price (USD)")

# Save chart as image
plt.savefig("chart.png")

# Show chart
plt.show()

print("Chart saved as chart.png")