import json
import pandas as pd

# Load JSON file
with open("crypto_data.json", "r") as file:
    data = json.load(file)

# Extract prices
prices = {
    "coin": ["bitcoin", "ethereum", "dogecoin"],
    "price_usd": [
        data["bitcoin"]["usd"],
        data["ethereum"]["usd"],
        data["dogecoin"]["usd"]
    ],
    "timestamp": data["timestamp"]
}

# Convert to DataFrame
df = pd.DataFrame(prices)

# Save processed data
df.to_csv("processed_crypto_data.csv", index=False)

print("Data processed and saved successfully!")
print(df)