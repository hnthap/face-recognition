import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml',
)


def detect_faces_haarcascade(image: np.ndarray, scale_factor, min_neighbors, min_size):
    image = cv2.resize(image, (image.shape[1] * 500 // image.shape[0], 500))
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=(min_size, min_size),
    )
    for (x, y, w, h) in faces:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

