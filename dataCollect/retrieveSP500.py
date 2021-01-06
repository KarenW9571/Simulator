import yfinance as yf
import pandas as pd
import pickle
import json


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
        if (df.shape == (0, 0)):
            df = adjPrice
        else:
            df = pd.merge(df, adjPrice, how="outer",
                          left_index=True, right_index=True)
    return df.round(2)


def initialDataLoad(tickerList, start="2019-10-18", end="2020-12-31"):
    output = {}
    for ticker in tickerList:
        data = yf.download(ticker, start, end)
        dataJs = data.to_json(orient="index")
        temp = {"Stock": ticker, "Price": dataJs}
        # need change to generate entire json
        output = json.dumps(temp)
        return output


stock = yf.download(tickers[0], start="2019-10-18", end="2020-12-31")
print(stock.head(5))
