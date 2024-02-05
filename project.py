import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class MovieRecommender:
    def __init__(self):
        self.movies = pd.read_csv('movies.csv')
        self.tf_idf_matrix = None
        self.movie_indices = None

    def preprocess_data(self):
        # Tratar os dados de gênero
        self.movies['genres'] = self.movies['genres'].fillna('')
        
        # Usar TF-IDF para vetorizar os gêneros
        tfidf = TfidfVectorizer(stop_words='english')
        self.tf_idf_matrix = tfidf.fit_transform(self.movies['genres'])

        # Mapear índices de filmes
        self.movie_indices = pd.Series(self.movies.index, index=self.movies['title'])

    def get_recommendations(self, title, num_recommendations=5):
        # Obter o índice do filme com base no título
        idx = self.movie_indices[title]

        # Calcular similaridade de cosseno
        cosine_sim = linear_kernel(self.tf_idf_matrix, self.tf_idf_matrix)

        # Obter as pontuações de similaridade dos filmes com o filme fornecido
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Ordenar os filmes com base nas pontuações de similaridade
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Obter os índices dos filmes recomendados
        movie_indices = [i[0] for i in sim_scores[1:num_recommendations+1]]

        # Retornar os títulos dos filmes recomendados
        return self.movies['title'].iloc[movie_indices]

# Exemplo de uso
if __name__ == "__main__":
    recommender = MovieRecommender()
    recommender.preprocess_data()

    movie_title = "GoldenEye (1995)"
    recommendations = recommender.get_recommendations(movie_title)
    print(f"Recomendações para '{movie_title}':")
    for movie in recommendations:
        print(movie)
