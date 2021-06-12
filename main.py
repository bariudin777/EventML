from DataBaseLogic.DBManager import DataBaseConnection
from DataBaseLogic.EventRecommendationController import EventRecommendationSchema

class Main:

    def __init__(self):
        self.db_manager = DataBaseConnection().createDataBaseClient()


if __name__ == '__main__':
    main = Main()

