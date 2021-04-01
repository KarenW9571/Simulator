import mysql.connector
import json
import pandas as pd
from sqlalchemy import create_engine


class database():
    def __init__(self):
        self.config = json.load(open('dataCollect/Config.json'))
        self.client = mysql.connector.connect(**self.config)
        self.engine = create_engine('mysql+pymysql://codeInteraction:Rachel.95@localhost/stockPrice')
        self.cursor = self.client.cursor()

    def disconnect(self):
        self.cursor.close()
        self.client.close()

    def getData(self, query):

        df = pd.read_sql(query, self.client)
        return df

    def insertData(self, tableName, dataFrame):
        try:
            dataFrame.to_sql(name = tableName, con = self.engine, if_exists='append',index= False)
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print("Table %s created successfully." % tableName)
