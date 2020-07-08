import streamlit as st
import math


def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        x_var = st.number_input('Insira o valor de 𝑥')
        k_var = st.number_input('Insira o valor de k')
        st.title("Se 𝑥 = {}".format(x_var))
        if k_var != 0 or x_var != 0:
            try:
                st.title("𝑓 (𝑥) = log{}({})".format(k_var, x_var))
                st.title("𝑓 ({}) = {:.4f}".format(x_var, math.log(x_var, k_var)))
            except:
                st.title("O valor atual é inválido, tente trocar o valor de X ou K")

    if opt == 'Derivada':
        x_var = st.number_input('Insira o valor de 𝑥')
        k_var = st.number_input('Insira o valor de k')
        st.title("Se 𝑥 = {}".format(x_var))
        if k_var != 0 or x_var != 0:
            try:
                st.title("𝑓' (𝑥) = log{}({})".format(k_var, x_var))
                st.title("𝑓' ({}) = log{}({})".format(x_var, k_var, x_var))
                st.title("𝑓' ({}) = 1/{}*ln({})".format(x_var, k_var, k_var))
                st.title("𝑓' ({}) = {:.4f}".format(x_var, 1/x_var*math.log(k_var)))
            except:
                st.title("O valor atual é inválido, tente trocar o valor de X ou K")

    if opt == 'Integral Definida':
        st.title("Integral Definida")
        st.title("Nao implementado")
