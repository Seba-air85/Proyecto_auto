import requests

API_KEY = "a8e852464b4d5b2534318baf"

url = f"https://v6.exchangerate-api.com/v6/a8e852464b4d5b2534318baf/latest/USD"

response = requests.get(url)

data = response.json()

print(data["conversion_rates"]["CLP"])
print(data["conversion_rates"]["EUR"])