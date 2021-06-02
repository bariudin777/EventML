import pandas as pd
from sklearn.neighbors import NearestNeighbors

from DataBaseLogic.EventRecomendatinSchema import EventRecommendationSchema


class KnnModel:
    '''Knn Model'''

    def __init__(self):
        s = EventRecommendationSchema()
        self.n_neighbors = 3
        self.df, self.payload = s.getData()
        self.df_copy = self.df.copy()

    def model(self, user, number_recommendations):
        knn = NearestNeighbors(metric='cosine', algorithm='brute')
        knn.fit(self.df.values)
        distances, indices = knn.kneighbors(self.df.values, n_neighbors=self.n_neighbors)

        user_index = self.df.columns.tolist().index(user)
        # row = row number of title in df, title= event title
        for row, title in list(enumerate(self.df.index)):
            # find event without ratings by user
            if self.df.iloc[row, user_index] == 0:
                sim_event = indices[row].tolist()
                event_dis = distances[row].tolist()
                self.removeFirst(sim_event, event_dis, row)
                event_similarity = [1 - x for x in event_dis]
                e_s_copy = event_similarity.copy()
                nominator = 0
                # for each similar event
                for s in range(0, len(event_similarity)):
                    # check if the rating of a similar event is zero
                    if self.df.iloc[sim_event, user_index] == 0:
                        if len(e_s_copy) == (self.n_neighbors - 1):
                            e_s_copy.pop(s)
                        else:
                            e_s_copy.pop(s - (len(event_similarity) - len(e_s_copy)))
                    # if the rating is not zero, use the rating and similarity in the calculation
                    else:
                        nominator = nominator + event_similarity[s] * self.df.iloc[sim_event[s], user_index]
                # check if the number of the ratings with non-zero is positive
                if len(e_s_copy) > 0:
                    if sum(e_s_copy) > 0:
                        prediction = nominator / sum(e_s_copy)
                    # Even if there are some event for which the ratings are positive, some event have zero similarity
                    # even though they are selected as similar events.
                    # in this case, the predicted rating becomes zero as well
                    else:
                        prediction = 0
                else:
                    prediction = 0
                # place the prediction
                self.df_copy.iloc[row, user_index] = prediction
        self.recomend_event(user,number_recommendations)



    ''' Remove the first event distence- clear data'''

    def removeFirst(self, sim_event, event_dis, row):
        if row in sim_event:
            event_id = sim_event.index(row)
            sim_event.remove(row)
            event_dis.pop(event_id)
        # if the last event has no ratings
        else:
            sim_event = sim_event[:self.n_neighbors - 1]
            event_dis = event_dis[:self.n_neighbors - 1]

    def recomend_event(self, user, number_recommendations):
        print('The list of the Event {} Has Watched \n'.format(user))

        for m in self.df[self.df[user] > 0][user].index.tolist():
            print(m)

        print('\n')

        recommended_events = []

        for m in self.df[self.df[user] == 0].index.tolist():
            index_df = self.df.index.tolist().index(m)
            predicted_rating = self.df_copy.iloc[index_df, self.df_copy.columns.tolist().index(user)]
            recommended_events.append((m, predicted_rating))

        sorted_rm = sorted(recommended_events, key=lambda x: x[1], reverse=True)

        print('The list of the Recommended Movies \n')
        rank = 1
        for recommended_event in sorted_rm[:number_recommendations]:
            print('{}: {} - predicted rating:{}'.format(rank, recommended_event[0], recommended_event[1]))
            rank = rank + 1


if __name__ == '__main__':
    model = KnnModel()
    model.model(1,5)