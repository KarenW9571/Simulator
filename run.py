from dataCollect.retrieveSP500 import initialDataLoad
from dataCollect.getTicker import save_sp500_tickers
import pickle

#with open("dataCollect/sp500tickers.pickle", "rb") as f:
#    tickers = pickle.load(f)
#print(tickers[0])
#initialDataLoad(tickers)
#weeklyInjection(tickers)

save_sp500_tickers()