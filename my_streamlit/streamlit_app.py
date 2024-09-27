import streamlit as st
import cv2
from model import face_equals


def equals(first_face, second_face):
    if first_face and second_face:
        cosine_dist = face_equals.get_cosine(cv2.imread(first_face), cv2.imread(second_face))

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
