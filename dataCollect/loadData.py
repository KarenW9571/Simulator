from . import dbConnect
from dataCollect.retrieveSP500 import initialDataLoad
from dataCollect.retrieveSP500 import additionalDataLoad
import pandas as pd
from datetime import datetime

class loadData(): 
    def __init__(self): 
        self.db = dbConnect.database()
        self.today = datetime.today().date()
    
    def getVariable(self, start,end,variable,ticker): 
        
        #determine if input of ticker exits in the table
        
        for t in ticker:
            query = """
            SELECT ticker 
            FROM stock.stockName 
            WHERE ticker = '%s'
            """ % (t)
            ls = self.db.getData(query)

            if len(ls) > 0: 
                pass 
            else: 
                print("%s does not exist in the database" % (t))
                print("Retrieving and injecting data for %s" % (t))
                additionalDataLoad(ticker = t)
                print("Data for %s injected" % (t))

        ticker = str(ticker).replace('[','').replace(']','')
        start = '"' + start + '"'
        end = '"' + end + '"'

        #composite query based on input
        query = """
        SELECT date,  %s ,ticker
        FROM stock.stockPrice 
        WHERE date BETWEEN  CAST( %s AS DATE) and CAST( %s  AS DATE)
            AND 
            ticker in ( %s )
        """ % (variable,start, end, ticker)

        #read query to df
        df = self.db.getData(query)
        output = pd.pivot_table(df, values=variable, index=['date'],columns=['ticker'])


        return output
    