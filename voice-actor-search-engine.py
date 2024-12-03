import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class VoiceActorReverseSearch:
    def __init__(self):
        # Initialize data storage and indexing components
        self.voice_actors_df = None
        self.feature_matrix = None
        self.vectorizer = None

    def load_voice_actor_data(self, csv_path):
        """
        Load voice actor data from a CSV file.
        Expected columns: name, roles, voice_type, genre_specialization
        """
        self.voice_actors_df = pd.read_csv(csv_path)

    def create_feature_matrix(self):
        """
        Create a feature matrix using TF-IDF vectorization
        to capture textual characteristics of voice actors
        """
        # Combine relevant text features
        combined_features = self.voice_actors_df.apply(
            lambda row: f"{row['name']} {row['roles']} {row['voice_type']} {row['genre_specialization']}", 
            axis=1
        )

        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.feature_matrix = self.vectorizer.fit_transform(combined_features)

    def find_similar_voice_actors(self, query, top_k=5):
        """
        Find voice actors similar to the input query
        """
        query_vector = self.vectorizer.transform([query])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(query_vector, self.feature_matrix)[0]
        
        # Get top K similar voice actors
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        return self.voice_actors_df.iloc[top_indices]

    def advanced_search(self, voice_characteristics):
        """
        Perform advanced search based on multiple voice characteristics
        """
        # Placeholder for more complex matching logic
        pass

# Example usage
reverse_search = VoiceActorReverseSearch()
reverse_search.load_voice_actor_data('voice_actors.csv')
reverse_search.create_feature_matrix()

# Find similar voice actors to a query
results = reverse_search.find_similar_voice_actors("heroic shonen protagonist")
print(results)
