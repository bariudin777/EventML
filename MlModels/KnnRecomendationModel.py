import pandas as pd
from sklearn.neighbors import NearestNeighbors

from DataBaseLogic.EventRecomendatinSchema import EventRecommendationSchema


class KnnModel:
    '''Knn Model'''
    def __init__(self):
        self.n_neighbors = 3

    def model(self, user, event_id):
        s = EventRecommendationSchema()
        df, payload = s.getData()
        knn = NearestNeighbors(metric='cosine', algorithm='brute')
        knn.fit(df.values)
        distances, indices = knn.kneighbors(df.values, n_neighbors=3)

        user_index = df.columns.tolist().index(user)
        # row = row number of title in df, title= event title
        for row, title in list(enumerate(df.index)):
            # find event without ratings by user
            if df.iloc[row, user_index] == 0:
                sim_event = indices[row].tolist()
                event_dis = distances[row].tolist()
                self.removeFirst(sim_event, event_dis, row)


    ''' Remove the first event distence- clear data'''
    def removeFirst(self, sim_event, event_dis, row):
        if row in sim_event:
            event_id = sim_event.index(row)
            sim_event.remove(row)
            event_dis.pop(event_id)
        #if the last event has no ratings
        else:
            sim_event = sim_event[:self.n_neighbors-1]
            event_dis = event_dis[:self.n_neighbors-1]




if __name__ == '__main__':
    model = KnnModel()
    model.recommend()
