from insightface.app import FaceAnalysis
import numpy as np
from PIL import Image


class FaceEquals:
    def __init__(self, face_analysis: FaceAnalysis):
        self.face_analysis = face_analysis

    def get_faces(self, img: np.ndarray) -> list:
        return self.face_analysis.get(img)

    def get_first_face(self, img: np.ndarray) -> np.array:
        x, y, x2, y2 = self.get_faces(img)[0].bbox
        cropped = img[int(y):int(y2), int(x):int(x2)]

        return cropped

    def get_distance(self, img_first: np.ndarray, img_second: np.ndarray) -> float:
        return np.linalg.norm(self.get_faces(img_first)[0].embedding -
                              self.get_faces(img_second)[0].embedding)

    def get_cosine(self, img_first: np.ndarray, img_second: np.ndarray) -> float:
        first_embedding = self.get_faces(img_first)[0].embedding
        second_embedding = self.get_faces(img_second)[0].embedding

        return np.dot(first_embedding, second_embedding) / (np.linalg.norm(first_embedding) * np.linalg.norm(second_embedding))


app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(256, 256))
face_equals = FaceEquals(app)
