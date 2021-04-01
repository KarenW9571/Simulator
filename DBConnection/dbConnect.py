import mysql.connector
import json


class database():

    def dbConnect(self):
        f = open('Config.json')
        config = json.load(f)
        client = mysql.connector.connect(**config)

        return client
