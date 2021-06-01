import DBManager


class EventRecommendationSchema:

    def __init__(self):
        self.collection_manager = ""


    def createSchemaManager(self):

        connection = DBManager.DataBaseConnection()  # create an database connection class
        self.collection_manager = connection.createDataBaseClient()  # get the client

    def createRecommendationSchema(self, data):
        ecommendation_sc = self.collection_manager.recommendationMatrix
        ecommendation_sc.insert_one(data)


