import streamlit as st
import cv2
import numpy as np
from model import face_equals


def equals(first_face, second_face):
    if first_face and second_face:
        first_face_bytes = np.asarray(bytearray(first_face.read()), dtype=np.uint8)
        second_face_bytes = np.asarray(bytearray(second_face.read()), dtype=np.uint8)
        img1 = cv2.imdecode(first_face_bytes, 1)
        img2 = cv2.imdecode(second_face_bytes, 1)
        cosine_dist = face_equals.get_cosine(img1, img2)

        st.image(face_equals.get_first_face(img1))
        st.image(face_equals.get_first_face(img2))
        if cosine_dist > 0.6:
            st.text('Лица одинаковые')
        else:
            st.text('Лица разные')
    else:
        st.error('Нужны 2 картинки с лицом')


st.title('Сравнение лиц')

face_1 = st.file_uploader(label='Лицо 1', type=['png', 'jpg'])

if face_1:
    st.image(face_1)

face_2 = st.file_uploader(label='Лицо 2', type=['png', 'jpg'])

if face_2:
    st.image(face_2)

if st.button('Сравнить'):
    equals(face_1, face_2)
