import pandas as pd


movies = pd.read_pickle('movie_matrix.pkl')

def recommended(movie_name,count):
    return list(movies[movie_name].sort_values(ascending=False)[1:count].index)


def list_of_movies():
    return movies.index

#recommended_movie=recommended("Avatar")
#print(recommended_movie)