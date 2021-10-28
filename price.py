#Problem checking
error = False
reason = ""

def problem(r):
    global error
    global reason
    
    error = True
    reason = reason + r + "\n"

try:
    #imports
    import pandas as pd
    import finnhub
    import yaml
except ModuleNotFoundError:
    problem("Certain packages not installed")

#objects
with open('config.yaml') as f:
    config = yaml.safe_load(f)

"""
f = open("stocks.csv", "w")
writer = csv.writer(f)    
"""
try:
    f = pd.read_csv("stocks.csv")
except FileNotFoundError:
    problem("stocks.csv does not exist")
    
finnhub_client = finnhub.Client(api_key=config[config["Finnhub_API-Key"])

#functions


def addStock(name):
    name = [name]
    writer.writerow(name)

    
#creates the csv
if error == False:
    header = ["name", "price", "change_points", "change_percent"]

    writer.writerow(header)
    addStock("APPL")

    f.close()
else:
    print(reason)                                              
print(finnhub_client.quote('AAPL'))                                      
