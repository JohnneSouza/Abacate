import streamlit as st


def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        st.title("Função")
        st.title("Nao implementado")

    if opt == 'Derivada':
        st.title("Derivada")
        st.title("Nao implementado")

    if opt == 'Integral Definida':
        st.title("Integral Definida")
        st.title("Nao implementado")
