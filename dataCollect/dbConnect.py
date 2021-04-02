import json
import pandas as pd
import sqlalchemy


class database():
    def __init__(self):
        #self.config = json.load(open('dataCollect/Config.json'))
        self.con = sqlalchemy.create_engine("mysql://root:Rachel.95@35.224.187.23/stock")
        #self.cursor = self.con.cursor()


    def getData(self, query):

        df = pd.read_sql(query, self.con)
        return df

    def insertData(self, tableName, dataFrame, if_exists='append'):
        try:
            dataFrame.to_sql(name = tableName, con = self.con, if_exists= if_exists ,index= False)
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print("Data inserted to %s successfully." % tableName)



