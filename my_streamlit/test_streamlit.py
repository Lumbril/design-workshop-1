from model import face_equals
import cv2


def test_empty():
    assert True is True


def test_equals():
    cosine_dist = face_equals.get_cosine(cv2.imread('images/конор 2.jpg'), cv2.imread('images/леброн 1.png'))
    assert cosine_dist < 0.6
