import pytest
from recommend import MovieRecommender

@pytest.fixture
def movie_recommender():
    return MovieRecommender()

def test_preprocess_data(movie_recommender):
    movie_recommender.preprocess_data()
    assert movie_recommender.tf_idf_matrix is not None
    assert movie_recommender.movie_indices is not None

def test_get_recommendations(movie_recommender):
    movie_recommender.preprocess_data()
    recommendations = movie_recommender.get_recommendations("GoldenEye (1995)", num_recommendations=3)
    assert len(recommendations) == 3
