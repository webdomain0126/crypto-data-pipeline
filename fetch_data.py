import requests
import json
from datetime import datetime

# API endpoint
url = "https://api.coingecko.com/api/v3/simple/price"

# parameters
params = {
    "ids": "bitcoin,ethereum,dogecoin",
    "vs_currencies": "usd"
}

# fetch data
response = requests.get(url, params=params)

data = response.json()

# add timestamp
data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# save to file
with open("crypto_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Crypto data saved successfully!")