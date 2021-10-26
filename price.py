import csv
import finnhub

finnhub_client = finnhub.Client(api_key="Your API Key")

f = open("stocks.csv", "w")
writer = csv.writer(f)

def addStock(name):
    name = [name]
    writer.writerow(name)

header = ["name", "price", "change_points", "change_percent"]

writer.writerow(header)
addStock("APPL")

f.close()
