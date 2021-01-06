import yfinance as yf
import pandas as pd
import pickle


'''
    For now, we only consider the stock prices, we could addin supplimentary information later.
'''
with open("sp500tickers.pickle", "rb") as f:
    tickers = pickle.load(f)
# This function is used to process the close price of the stock
def adjustClosePrice(tickerList, start="2019-10-18", end="2020-12-31"):
    df = pd.DataFrame()
    for ticker in tickerList:
        adjPrice = yf.download(ticker, start, end)[["Adj Close"]]
        adjPrice = adjPrice.rename(columns={"Adj Close": ticker})
        if (df.shape == (0,0)):
            df = adjPrice
        else:
            df = pd.merge(df, adjPrice, how = "outer", left_index=True, right_index=True)
    return df.round(2)


stock = yf.download(tickers[0], start="2019-10-18", end="2020-12-31")
print(stock.head(5))
