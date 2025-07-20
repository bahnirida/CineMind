import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from recommender.models import Movie

def get_similar_movies(movie_id, top_n=5):
    movies = list(Movie.objects.values('movieId', 'title', 'genres'))
    df = pd.DataFrame(movies)
    df['genres'] = df['genres'].fillna('')
    genres_matrix = df['genres'].str.get_dummies(sep='|')
    cos_sim = cosine_similarity(genres_matrix)

    idx = df[df['movieId'] == movie_id].index[0]
    similar_indices = cos_sim[idx].argsort()[::-1][1:top_n+1]
    return df.iloc[similar_indices][['movieId', 'title']]
