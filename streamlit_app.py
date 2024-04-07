import streamlit as st

st.title('Botón de alternancia en Streamlit')

# Definir un checkbox con un valor inicial False
toggle_button = st.checkbox('Activar/Desactivar')

# Verificar si el checkbox está marcado
if toggle_button:
    st.write('El botón de alternancia está activado.')
else:
    st.write('El botón de alternancia está desactivado.')
