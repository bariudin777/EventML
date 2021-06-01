import pymongo
from pymongo import MongoClient


class DataBaseConnection:

    def __init__(self):
        self.port = "27017"
        self.ip = "127.0.0.1"

    def establishconnection(self):
        try:
            address = "mongodb://" + self.ip + ":" + self.port + "/"
            client = pymongo.MongoClient(address)
            return client
        except():
            raise TypeError("data base connection error")

    def createDataBaseClient(self):
        try:
            client = self.establishconnection()
            data_base = client['MEANStackDB']
            return data_base
        except():
            raise TypeError("data base connection error")

    # reco_collection = data_base.recomendation
    # record = {
    #     "hgello": "akjdflka"
    # }
    # reco_collection.insert_one(record)
