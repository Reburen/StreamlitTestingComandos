import streamlit as st

st.title('Ejemplo de agregar botones después de hacer clic')

# Variable de estado para controlar si se ha hecho clic en el primer botón
boton1_clickeado = st.button('Botón 1')

# Si se hace clic en el Botón 1
if boton1_clickeado:
    st.write('Has presionado el Botón 1.')
    # Aquí puedes agregar código adicional que deseas ejecutar después de hacer clic en el Botón 1
    
    # Agregar más botones después de hacer clic en el Botón 1
   # boton2_clickeado = st.button('Botón 2')
 #   boton3_clickeado = st.button('Botón 3')

    # Si se hace clic en el Botón 2
boton2_clickeado = st.button('Botón 2')
boton3_clickeado = st.button('Botón 3')
if boton2_clickeado:
        st.write('Has presionado el Botón 2.')
        # Coloca aquí el código correspondiente al Botón 2
    
    # Si se hace clic en el Botón 3
if boton3_clickeado:
        st.write('Has presionado el Botón 3.')
        # Coloca aquí el código correspondiente al Botón 3

