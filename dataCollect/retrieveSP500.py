from . import dbConnect
import yfinance as yf
import pandas as pd
import pickle
import json
from datetime import datetime, timedelta



'''
    For now, we only consider the stock prices, we could addin supplimentary information later.
'''




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


def initialDataLoad(tickerList, start="2021-01-01", end="2021-04-02"):
    
    for ticker in tickerList:
        
        app = yf.download(ticker, start, end)
        app.reset_index(inplace=True)
        app = app.rename(columns={"Open": "openPrice",
                             "Close": "closePrice",
                             "High": "highPrice",
                             "Low": "lowPrice",
                             "Volume": "volume",
                             "Date": "date",
                             "Adj Close": "adjustedClose"
                             })
        app['ticker'] = ticker
        db = dbConnect.database()
        db.insertData(tableName = 'stockPrice', dataFrame = app)
    

def weeklyInjection(tickerList): 
    today = datetime.today().date()
    start = str(today - timedelta(7))
    end = str(today)
    
    initialDataLoad(tickerList, start=start, end=end)

def additionalDataLoad(ticker, start="2015-01-01", end= datetime.today().date()):  
    app = yf.download(ticker, start, end)
    app.reset_index(inplace=True)
    app = app.rename(columns={"Open": "openPrice",
                            "Close": "closePrice",
                            "High": "highPrice",
                            "Low": "lowPrice",
                            "Volume": "volume",
                            "Date": "date",
                            "Adj Close": "adjustedClose"
                            })
    app['ticker'] = ticker
    db = dbConnect.database()
    db.insertData(tableName = 'stockPrice', dataFrame = app)
    print('%s added to stockPrice table' % (ticker))
    
    ls = []
    ls.append(ticker)
    d = {'ticker': ls}
    tik = pd.DataFrame(d)
    db.insertData(tableName = 'stockName', dataFrame = tik)
    print('%s added to stockName table' % (ticker))



if __name__ == "__main__":

    stock = yf.download(tickers[0], start="2019-10-18", end="2020-12-31")
    print(stock.head(5))
    initialDataLoad(tickers)
