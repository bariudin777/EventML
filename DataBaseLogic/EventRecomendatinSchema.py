import DBManager
import pandas as pd
import json

class EventRecommendationSchema:


    def createSchemaManager(self):
        connection = DBManager.DataBaseConnection()  # create an database connection class
        collection_manager = connection.createDataBaseClient()  # get the client
        return collection_manager

    def createRecommendationSchema(self, data):
        collection_manager = self.createSchemaManager()
        recommendation_sc = collection_manager.recommendationMatrix
        recommendation_sc.insert_many(data)

    def insertMartrix(self):
        data = self.getData()
        self.createRecommendationSchema(data)

    def getData(self):
        df = pd.read_csv("../Ratings/recommendatin_ratings.csv")
        payload = json.loads(df.to_json(orient='records'))
        print(payload)
        return payload



        # record = {
        #     "hgello": "akjdflka"
        # }
        # return record


if __name__ == '__main__':
    event = EventRecommendationSchema()
    event.insertMartrix()
