import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Define the ratings matrix (example data)
ratings_matrix = {
    'User1': [5, 4, 0, 2, 1],
    'User2': [4, 0, 0, 5, 0],
    'User3': [0, 0, 4, 0, 0],
    'User4': [0, 2, 3, 4, 5],
    'User5': [1, 3, 2, 4, 5]
}

# Convert ratings matrix to a numpy array for cosine similarity calculation
users = list(ratings_matrix.keys())
ratings = np.array(list(ratings_matrix.values()))

# Step 2: Calculate the cosine similarity between users
cosine_sim = cosine_similarity(ratings)

# Print Original Ratings Matrix
print("Original Ratings Matrix:")
print("\t", "\t".join([f"Movie{i+1}" for i in range(ratings.shape[1])]))
for user, ratings in zip(users, ratings_matrix.values()):
    print(f"{user}\t", "\t".join(map(str, ratings)))

# Step 3: Calculate Cosine Similarity Matrix
print("\nCosine Similarity Matrix:")
print("\t", "\t".join(users))
for i, user_i in enumerate(users):
    print(user_i, "\t", "\t".join([f"{cosine_sim[i][j]:.6f}" for j in range(len(users))]))

# Step 4: Recommend movies based on cosine similarity
def recommend_movies(user, ratings_matrix, cosine_sim, top_n=3):
    user_idx = users.index(user)
    
    # Find similar users based on cosine similarity
    similar_users_idx = np.argsort(cosine_sim[user_idx])[::-1][1:]  # Exclude the user itself (highest similarity = 1)
    
    # Create a dictionary to store the scores for each movie
    movie_scores = {f"Movie{i+1}": 0 for i in range(len(ratings_matrix[user]))}
    
    # For each similar user, add their ratings to the movie scores
    for idx in similar_users_idx:
        similar_user = users[idx]
        for i, rating in enumerate(ratings_matrix[similar_user]):
            if rating > 0:  # Only consider rated movies
                movie_scores[f"Movie{i+1}"] += rating * cosine_sim[user_idx][idx]
    
    # Sort movies by score and return the top N recommendations
    recommended_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in recommended_movies[:top_n]]

# Step 5: Get recommendations for each user
for user in users:
    recommended = recommend_movies(user, ratings_matrix, cosine_sim)
    print(f"\nMovies recommended for {user}: {recommended}")
