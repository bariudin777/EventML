import pymongo
from pymongo import MongoClient

'''
Methods to write
1. connect to db
2. get movies from db
3. add set of movies to db



'''

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
data_base = client['MEANStackDB']
reco_collection = data_base.recomendation
record = {
    "hgello": "akjdflka"
}
reco_collection.insert_one(record)