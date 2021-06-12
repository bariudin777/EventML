import pymongo
'''
Data Base Manager
1. Create connections to data base
2. Create data base client
'''

class DataBaseConnection:

    def __init__(self):
        self.port = "27017"
        self.ip = "127.0.0.1"

    def establishConnection(self):
        try:
            address = "mongodb://" + self.ip + ":" + self.port + "/"
            client = pymongo.MongoClient(address)
            return client
        except():
            raise TypeError("data base connection error")

    def createDataBaseClient(self):
        try:
            client = self.establishConnection()
            data_base = client['MEANStackDB']
            return data_base
        except():
            raise TypeError("data base connection error")


