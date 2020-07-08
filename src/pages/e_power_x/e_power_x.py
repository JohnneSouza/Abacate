import streamlit as st
import numpy as np

#TODO ADICIONAR VIDEOS
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
        x_var = st.number_input('Insira o valor de (𝑥)')
        st.title("Se 𝑥 = {}".format(x_var))
        try:
            st.title("𝑓' (𝑥) = {}^{}".format("e", x_var))
            st.title("𝑓' ({}) = {}^{}".format(x_var, "e", x_var))
            st.title("𝑓 ({}) = {:.4f}".format(x_var, np.e**x_var))
        except:
            st.title("O valor atual é inválido, tente trocar o valor de X")

    if opt == 'Integral Definida':
        x_var = st.number_input('Insira o valor de (𝑥)')
        st.title("Se 𝑥 = {}".format(x_var))
        try:
            st.title("∫ 𝑓(𝑥)d𝑥 = {}^{} + C".format("e", x_var))
            st.title("{}^{} + C".format("e", x_var))
        except:
            st.title("O valor atual é inválido, tente trocar o valor de X")
