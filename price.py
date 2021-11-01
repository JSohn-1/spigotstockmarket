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
with open('D:\Library\Projects\Minecraft_Plugins\config.yaml') as f:
    config = yaml.safe_load(f)
print(config)

try:
    f = pd.read_csv(config["stocks"]["Path"])
    print("Test")
except FileNotFoundError:
    problem(config["stocks"]["Path"] + " does not exist")


finnhub_client = finnhub.Client(api_key=config["stocks"]["Finnhub_API-Key"])

#functions
"""
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
"""                                              
d=finnhub_client.quote('AAPL')
df=pd.DataFrame(data=d)
df.to_csv('Stocks.csv', sep ='\t')
new_df = pd.read_csv('Stocks.csv')
price=new_df['c']
print('Data from Stocks.csv:')
print(new_df)
print(price)
