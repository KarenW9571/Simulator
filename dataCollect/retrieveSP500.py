from DBConnection.dbConnect import database
import yfinance as yf
import pandas as pd
import pickle
import json


'''
    For now, we only consider the stock prices, we could addin supplimentary information later.
'''
with open("dataCollect/sp500tickers.pickle", "rb") as f:
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


def initialDataLoad(tickerList, start="2015-01-01", end="2020-12-31"):

    for ticker in tickerList:
        data = yf.download(ticker, start, end)
        data.rename(columns={"Open": "openPrice",
                             "Close": "closePrice",
                             "High": "highPrice",
                             "Low": "lowPrice",
                             "Volumn": "volumn"
                             })
        db = database()
        db.insertData('stockPrice', data)
        db.disconnect()


if __name__ == "__main__":

    stock = yf.download(tickers[0], start="2019-10-18", end="2020-12-31")
    print(stock.head(5))
    initialDataLoad(tickers)
