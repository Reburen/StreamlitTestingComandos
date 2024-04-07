import streamlit as st

st.title('Opción con dos botones en Streamlit')

button1_clicked = st.button('Botón 1')
button2_clicked = st.button('Botón 2')

if button1_clicked:
    st.write('Has presionado el Botón 1.')
    # Coloca aquí el código correspondiente al Botón 1
    button3_clicked = st.button('Botón 3')
    button4_clicked = st.button('Botón 4')
    if button3_clicked:
        st.write('Botón 3')
    if Button4_clicked:
        st.write('Botón 4')

if button2_clicked:
    st.write('Has presionado el Botón 2.')
    # Coloca aquí el código correspondiente al Botón 2
    button3_clicked = st.button('Botón 3')
    button4_clicked = st.button('Botón 4')
    if button3_clicked:
        st.write('Botón 3')
    if Button4_clicked:
        st.write('Botón 4')
