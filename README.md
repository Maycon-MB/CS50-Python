# Movie Recommendation System

## English

This project implements a movie recommendation system using content-based filtering. It suggests similar movies based on the characteristics of movies already watched by a user. The system uses TF-IDF (Term Frequency-Inverse Document Frequency) to vectorize the genres of movies and calculates similarity between movies using the cosine of TF-IDF vectors.

### Files

- **recommend.py**: Contains the implementation of the recommendation system.
- **test_recommend.py**: Contains unit tests for the functions in `recommend.py`.
- **movies.csv**: A CSV file containing movie data, including `movieId`, `title`, and `genres` fields.
- **requirements.txt**: List of project dependencies.

### How to Use

1. **Install Dependencies**:
   - Make sure you have Python 3.x installed on your system.
   - Install dependencies by running the following command in the terminal:
     ```
     pip install -r requirements.txt
     ```

2. **Run the Recommendation System**:
   - Execute the `recommend.py` file to see recommendations for a specific movie.
     ```
     python recommend.py
     ```

3. **Run Unit Tests**:
   - Execute the following command to run unit tests:
     ```
     pytest test_recommend.py
     ```

### Example Usage

```python
# Example usage of the recommendation system
if __name__ == "__main__":
    recommender = MovieRecommender()
    recommender.preprocess_data()

    movie_title = "GoldenEye (1995)"
    recommendations = recommender.get_recommendations(movie_title)
    print(f"Recommendations for '{movie_title}':")
    for movie in recommendations:
        print(movie)


