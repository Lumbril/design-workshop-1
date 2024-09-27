import numpy as np

from model import face_equals
import cv2
from PIL import Image


def test_empty():
    assert True is True


def test_equals():
    cosine_dist = face_equals.get_cosine(cv2.imread('images/конор 2.jpg'), cv2.imread('images/леброн 1.png'))
    assert cosine_dist < 0.6


def test_equals_from_image_open():
    img1 = Image('images/конор 2.jpg')
    img2 = Image('images/леброн 1.png')

    cosine_dist = face_equals.get_cosine(np.ndarray(img1), np.ndarray(img2))
    assert cosine_dist < 0.6
