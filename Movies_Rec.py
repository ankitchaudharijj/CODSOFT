
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv("movies.csv")

# Replace NaN with an empty string
movies["genre"] = movies["genre"].fillna("")

# Convert genres to vectors
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genre"])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Get the index of a movie by title
indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()

def recommend(title, num_recommendations=5):
    if title not in indices:
        return f"Movie '{title}' not found in the dataset."
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies["title"].iloc[movie_indices]

# Example
if __name__ == "__main__":
    movie = "Thor"
    print(f"Movies similar to '{movie}':\n")
    recommendations = recommend(movie)
    print(recommendations.to_string(index=False))
