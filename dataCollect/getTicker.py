# automating getting the S&P 500 list data, remember to update the list regularly
from . import dbConnect
import bs4 as bs  # beautiful soup
import pandas as pd
import requests  # can grab the saurce code from Wikipedia's page


def save_sp500_tickers():
    resp = requests.get(
        'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    companys = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text[:-1]
        tickers.append(ticker)
        company = row.findAll('td')[1].text[:-1]
        companys.append(company)

    d =  {'company':companys,'ticker':tickers}
    ticker = pd.DataFrame(d)

    db = dbConnect.database()
    db.insertData(tableName = 'stockName', dataFrame = ticker, if_exists='replace')
    
#save_sp500_tickers()
