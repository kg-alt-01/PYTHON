import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from tabulate import tabulate

movies_url = r"movies.csv"
ratings_url = r"ratings.csv"

movies = pd.read_csv(movies_url)
ratings = pd.read_csv(ratings_url)

data = pd.merge(ratings, movies, on='movieId')

user_item_matrix = data.pivot_table(index='userId', columns='title', values='rating').fillna(0)

svd = TruncatedSVD(n_components=50)
svd.fit(user_item_matrix)

predicted_ratings = svd.inverse_transform(svd.transform(user_item_matrix))

predicted_ratings_df = pd.DataFrame(predicted_ratings, index=user_item_matrix.index, columns=user_item_matrix.columns)

def recommend_movies(user_id, top_n=10):
    user_ratings = predicted_ratings_df.loc[user_id]
    sorted_ratings = user_ratings.sort_values(ascending=False)
    recommended_movies = sorted_ratings.index[~sorted_ratings.index.isin(user_item_matrix.loc[user_id].replace(0, np.nan).dropna().index)]
    return recommended_movies[:top_n]

user_id = 1
recommended_movies = recommend_movies(user_id)
print(f"Top 10 movie recommendations for User {user_id}:")
print(tabulate(pd.DataFrame(recommended_movies)))

user_id = 2
recommended_movies = recommend_movies(user_id)
print(f"Top 10 movie recommendations for User {user_id}:")
print(tabulate(pd.DataFrame(recommended_movies)))
