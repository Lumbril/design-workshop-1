import streamlit as st
import cv2
import numpy as np
from model import face_equals


def equals(first_face, second_face):
    if first_face and second_face:
        first_face_bytes = np.asarray(bytearray(first_face.read()), dtype=np.uint8)
        second_face_bytes = np.asarray(bytearray(second_face.read()), dtype=np.uint8)
        cosine_dist = face_equals.get_cosine(cv2.imdecode(first_face_bytes, 1), cv2.imdecode(second_face_bytes, 1))

        if cosine_dist > 0.6:
            st.text('Лица одинаковые')
        else:
            st.text('Лица разные')
    else:
        st.error('Нужны 2 картинки с лицом')


st.title('Сравнение лиц')

face_1 = st.file_uploader(label='Лицо 1', type=['png', 'jpg'])
face_2 = st.file_uploader(label='Лицо 2', type=['png', 'jpg'])

if st.button('Сравнить'):
    equals(face_1, face_2)
