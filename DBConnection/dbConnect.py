import mysql.connector
import json
import pandas as pd


class database():
    def __init__(self):
        self.config = json.load(open('Simulator/DBConnection/Config.json'))
        self.client = mysql.connector.connect(**self.config)
        self.cursor = self.client.cursor()

    def disconnect(self):
        self.cursor.close()
        self.client.close()

    def getData(self, query):

        df = pd.read_sql(query, self.client)
        return df

    def insertData(self, tableName, dataFrame):
        try:
            dataFrame.to_sql(tableName, self.client, if_exists='fail')
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print("Table %s created successfully." % tableName)
