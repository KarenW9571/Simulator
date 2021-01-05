import pymongo
import urllib


def dbConnect():
    mongo_uri = "mongodb+srv://karen:Rachel.95@1cluster0.6xfbw.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(mongo_uri)

    return client
