import streamlit as st
import math


def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        x_var = st.number_input('Insira o valor de 𝑥 (Ângulo) rad')
        st.title("Se 𝑥 = {} rad".format(x_var))
        try:
            st.title("𝑓 (𝑥) = sen(x)".format(x_var))
            st.title("𝑓 ({}) = {:.4f}".format(x_var, math.sin(math.radians(x_var))))
        except:
            st.title("Valor inválido, tente trocar o valor de X")

    if opt == 'Derivada':
        x_var = st.number_input('Insira o valor de 𝑥 (Ângulo) rad')
        st.title("Se 𝑥 = {} rad".format(x_var))
        try:
            st.title("𝑓' (𝑥) = sen(x)".format(x_var))
            st.title("𝑓' sen({}) = cos({})".format(x_var, x_var))
            st.title("cos({}) = {:.4f}".format(x_var, math.cos(math.radians(x_var))))
        except:
            st.title("Valor inválido, tente trocar o valor de X")

    if opt == 'Integral Definida':
        st.title("Integral Definida")
        st.title("Nao implementado")
