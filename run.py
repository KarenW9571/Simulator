from dataCollect.retrieveSP500 import initialDataLoad
import pickle

with open("dataCollect/sp500tickers.pickle", "rb") as f:
    tickers = pickle.load(f)
print(tickers[0])
initialDataLoad(tickers)
#weeklyInjection(tickers)