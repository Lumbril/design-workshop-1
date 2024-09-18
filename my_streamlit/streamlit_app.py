import streamlit as st


def equals(first_face, second_face):
    if first_face and second_face:
        print('Отправка лиц на сервер')
    else:
        print('Неполные данные')


st.title('Сравнение лиц')

face_1 = st.file_uploader(label='Лицо 1', type=['png', 'jpg'])
face_2 = st.file_uploader(label='Лицо 2', type=['png', 'jpg'])

if st.button('Сравнить'):
    equals(face_1, face_2)
