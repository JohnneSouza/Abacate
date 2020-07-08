import streamlit as st
import math

INVALID_VALUE = "Valor inválido, tente trocar o valor de X"

#TODO IMPLEMENTAR SECANTE
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
        x_var = st.number_input('Insira o valor de 𝑥 (Ângulo) rad')
        st.title("Se 𝑥 = {} rad".format(x_var))
        try:
            st.title("𝑓' (𝑥) = tan(x)".format(x_var))
            st.title("𝑓' tan({}) = sec^2({})".format(x_var, x_var))
            #st.title("sec({}) = {:.4f}".format(x_var, -1 * math.(math.radians(x_var))))
        except:
            st.title("Valor inválido, tente trocar o valor de X")

    if opt == 'Integral Definida':
        st.title("Integral Definida")
        st.title("Nao implementado")
