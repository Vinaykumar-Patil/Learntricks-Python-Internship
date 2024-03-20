'''Movie Recommendation System: Build a simple movie recommendation system that 
suggests movies to users based on their preferences and ratings.'''

import pandas as pd

# Creating sample movie ratings data
ratings_data = {
    'Movie': ['12th Fail', 'Ramayana : The Legend of Prince Rama', 'Nayakan', 'Gol Maal', 
              'Rocketry: The Nambi Effect', '777 Charlie'],
    'Rating': [9.0, 9.2, 8.7, 8.5, 8.7, 8.7]
}

# Createing DataFrame from ratings data
ratings_df = pd.DataFrame(ratings_data)

# Defining Function to recommend movies based on rating threshold
def recommend_movies_above_rating(ratings_df, rating_threshold):
    # Filter movies with ratings above the specified threshold
    recommended_movies = ratings_df[ratings_df['Rating'] > rating_threshold]

    return recommended_movies['Movie'].tolist()

# Defining Main function
def main():
    # Get user's rating threshold
    rating_threshold = float(input("Enter your rating threshold (e.g.,1.0, 2.5, 8.0): "))

    # Get recommended movies above the rating threshold
    recommended_movies = recommend_movies_above_rating(ratings_df, rating_threshold)
    if recommended_movies:
        print(f"Recommended movies with ratings above {rating_threshold}:")
        for movie in recommended_movies:
            print(movie)
    else:
        print(f"No movies found with ratings above {rating_threshold}")

if __name__ == "__main__":
    main()
