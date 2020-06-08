import streamlit as st


def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))
    if st.button('Iniciar'):
        st.write(opt)