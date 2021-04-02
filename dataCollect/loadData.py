from . import dbConnect
import pandas as pd

class loadData(): 
    def __init__(self): 
        self.db = dbConnect.database()
    
    def getVariable(self, start,end,variable,ticker): 
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

        #pivot table 

        return output
    