import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row


def get_similar_events(event_name, user_rating):
    similar_score = item_similarity_df[event_name] * (user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score


if __name__ == '__main__':
    ratings = pd.read_csv('../Ratings/RatingsForCosine.csv', index_col=0)
    ratings = ratings.fillna(0)
    ratings_std = ratings.apply(standardize)
    item_similarity = cosine_similarity(ratings_std.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=ratings.columns, columns=ratings.columns)

    print(get_similar_events("e1", 1))
