#imports
import pandas as pd
import finnhub
import yaml

#objects
with open('config.yaml') as f:
    config = yaml.safe_load(f)

"""
f = open("stocks.csv", "w")
writer = csv.writer(f)    
"""

f = pd.read(

finnhub_client = finnhub.Client(api_key=config[config["Finnhub_API-Key"])

#variables
error = False
reason = ""

#functions
def problem(r):
    global error
    global reason
    
    error = True
    reason = reason + r + "\n"

def addStock(name):
    name = [name]
    writer.writerow(name)

    
#creates the csv
if error == False:
    header = ["name", "price", "change_points", "change_percent"]

    writer.writerow(header)
    addStock("APPL")

    f.close()
