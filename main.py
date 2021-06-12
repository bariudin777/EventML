from DataBaseLogic.EventRecommendationController import EventRecommendationSchema
from MlModels.KnnRecomendationModel import KnnModel

FIRST_INIT = True

if __name__ == '__main__':
    controller = EventRecommendationSchema()
    if FIRST_INIT:
        controller.insertMartrix()
    number_of_neighbors = 3
    knn_model = KnnModel(controller, number_of_neighbors)
    knn_model.model("user_3", 3)
