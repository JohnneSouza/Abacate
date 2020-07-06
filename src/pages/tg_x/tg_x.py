import streamlit as st
import math

INVALID_VALUE = "Valor inválido, tente trocar o valor de X"


def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        x_var = st.number_input('Insira o valor de 𝑥 (Ângulo) rad')
        st.title("Se 𝑥 = {} rad".format(x_var))
        if x_var % 90 != 0:
            try:
                st.title("𝑓 (𝑥) = tan(x)".format(x_var))
                st.title("𝑓 ({}) = {:.4f}".format(x_var, math.tan(math.radians(x_var))))
            except:
                st.title(INVALID_VALUE)
        if x_var % 90 == 0:
            st.title(INVALID_VALUE)

    if opt == 'Derivada':
        st.title("Derivada")
        st.title("Nao implementado")

    if opt == 'Integral Definida':
        st.title("Integral Definida")
        st.title("Nao implementado")
