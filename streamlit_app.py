import streamlit as st

# Verifica si los botones se han inicializado en la sesión
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False

# Primer botón
button1_clicked = st.button('Botón 1')

# Si se hace clic en el Botón 1
if button1_clicked:
    st.session_state.button1_clicked = True

# Verifica si los botones se han inicializado en la sesión
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False

# Segundo botón
button2_clicked = st.button('Botón 2')

# Si se hace clic en el Botón 2
if button2_clicked:
    st.session_state.button2_clicked = True

# Imprimir el estado de los botones
st.write('Estado del Botón 1:', st.session_state.button1_clicked)
st.write('Estado del Botón 2:', st.session_state.button2_clicked)
