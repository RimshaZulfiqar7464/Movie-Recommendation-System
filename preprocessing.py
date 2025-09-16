import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_similarity():
    movies = pd.read_csv("data/tmdb_5000_movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")
    movies = movies.merge(credits, on="title")

    movies['tags'] = movies['overview'].fillna("")

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()

    similarity = cosine_similarity(vectors)

    os.makedirs("model", exist_ok=True)
    pickle.dump(movies, open("model/movie_list.pkl", "wb"))
    pickle.dump(similarity, open("model/similarity.pkl", "wb"))
    print("✅ Pickle files saved in model/")

if __name__ == "__main__":
    create_similarity()

