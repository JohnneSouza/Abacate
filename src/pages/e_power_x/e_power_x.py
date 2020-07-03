import streamlit as st
import numpy as np


def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        x_var = st.number_input('Insira o valor de (𝑥)')
        st.title("Se 𝑥 = {}".format(x_var))
        try:
            st.title("𝑓 (𝑥) = {}^{}".format("e", x_var))
            st.title("𝑓 ({}) = {:.4f}".format(x_var, np.e**x_var))
        except:
            st.title("O valor atual é inválido, tente trocar o valor de X")


    if opt == 'Derivada':
        st.title("Derivada")
        st.title("Nao implementado")

    if opt == 'Integral Definida':
        st.title("Integral Definida")
        st.title("Nao implementado")
