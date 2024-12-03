import librosa
import numpy as np
from sklearn.neighbors import NearestNeighbors

class VoiceActorRecognition:
    def __init__(self, voice_actor_data):
        self.voice_actor_data = voice_actor_data
        self.features = self.extract_features(self.voice_actor_data)
        self.model = NearestNeighbors(n_neighbors=1)
        self.model.fit(self.features)

    def extract_features(self, data):
        features = []
        for sample in data:
            audio, _ = librosa.load(sample['audio_path'], sr=16000)
            mfcc = librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=40)
            features.append(np.mean(mfcc, axis=1))
        return np.array(features)

    def recognize_voice_actor(self, audio_path):
        audio, _ = librosa.load(audio_path, sr=16000)
        query_features = np.mean(librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=40), axis=1)
        distances, indices = self.model.kneighbors([query_features])
        return self.voice_actor_data[indices[0][0]]
