import csv
import finnhub

finnhub_client = finnhub.Client(api_key="c5ro3eaad3ifnpn57lmg")

f = open("stocks.csv", "w")
writer = csv.writer(f)

def addStock(name):
    name = [name]
    writer.writerow(name)

header = ["name", "price", "change_points", "change_percent"]

writer.writerow(header)
addStock("APPL")

f.close()

#print(finnhub_client.company_eps_estimates('APPL', freq='quarterly'))

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=15min&apikey=DECGTCKXGVWZB116'
r = requests.get(url)
data = r.json()

print(data)
