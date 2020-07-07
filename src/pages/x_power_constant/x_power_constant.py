import streamlit as st
import math


# TODO TROCAR LINK DOS VIDEOS
def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        x_var = st.number_input('Insira o valor de (x)')
        k_var = st.number_input('Insira o valor de (k)')

        st.title("𝑓 (𝑥) = x^k")
        try:
            if x_var > 50 or k_var > 50:
                st.title("Valores muito grandes podem causa problemas, cuidado.⚠")
            st.title("𝑓 (𝑥) = {: .2f}".format(x_var ** k_var))
        except:
            st.title("Valor inválido, tente trocar o valor de X ou K")

        st.markdown(
            """
            Veja mais detalhes neste [video](https://www.youtube.com/watch?v=ivRjk7T6AXw) sobre funções
            """
        )


    if opt == 'Derivada':
        st.title("Derivada")
        x_var = st.number_input('Insira o valor de (𝑥)')
        k_var = st.number_input('Insira o valor de (k)')

        if k_var != 0 or x_var != 0:
            try:
                st.title("Se 𝑥 = {} e k = {}".format(x_var, k_var))
                st.title("𝑓' (𝑥) = {}^{}*{}({})".format("k", "𝑥", "ln", "k"))
                st.title("𝑓' (𝑥) = {}^{}*{}({}))".format(k_var, x_var, "ln", k_var))
                st.title("𝑓' ({}) = {}*ln({})".format(x_var, k_var**x_var, x_var))
                st.title("𝑓' ({}) = {:.4f} (decimal)".format(x_var, k_var ** x_var * math.log(k_var)))
            except:
                st.title("O valor atual é inválido, tente trocar o valor de X ou K")

        st.markdown(
            """
            Veja mais detalhes neste [video](https://www.youtube.com/watch?v=nfARXFLUKMc) sobre Derivada da Função Exponencial.
            """
        )


    if opt == 'Integral Definida':
        st.title("O nome Integral Definida vem do fato que a integral está restrita a um intervalo.")
        st.number_input('Insira o valor de (x)')
        st.write("𝑓' (𝑥) = " + str(0))
        st.markdown(
            """
            Veja mais detalhes neste [site](https://www.dicasdecalculo.com.br/conteudos/integrais/integral-definida/) sobre integrais definidas.
            """
        )
