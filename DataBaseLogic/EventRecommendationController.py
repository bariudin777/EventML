import pandas as pd
import json
from DataBaseLogic.DBManager import DataBaseConnection


class EventRecommendationSchema:
    def __init__(self):
        self.db_manager = DataBaseConnection().createDataBaseClient() # create db client

    def insertMartrix(self):
        '''insert matrix to data base'''
        data = self.getData()
        self.createRecommendationMatrix(data, self.db_manager)

    def createRecommendationMatrix(self, data, dbManager):
        '''uses the data manager to insert recommendation matrix to data base'''
        recommendation_sc = dbManager.recommendationMatrix
        recommendation_sc.insert_many(data)

    def getData(self):
        '''Gets the data from csv file'''
        df = pd.read_csv("../Ratings/recommendatin_ratings.csv")
        payload = json.loads(df.to_json(orient='records'))
        return df, payload


