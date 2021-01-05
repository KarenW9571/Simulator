import pymongo
import urllib


def dbConnect():
    mongo_uri = "mongodb+srv://karen:Rachel.95@cluster0.6xfbw.mongodb.net/test?retryWrites=true&w=majority"

    client = pymongo.MongoClient(mongo_uri)

    return client
