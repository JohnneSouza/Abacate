import streamlit as st
import matplotlib.pyplot as plt

def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        st.title("Em matemática, uma função constante é uma função cujo valor (de saída) é o mesmo para todos os "
                 "valores de entrada")
        const = st.number_input('Insira o valor de (x)')
        st.title("𝑓 (𝑥) = " + "{:.4f}".format(const))

        plt.axhline(y=const, color='r', linestyle='-')
        plt.title('Grafico da Função')
        st.pyplot()

        st.markdown(
            """
            Veja mais detalhes neste [video](https://www.youtube.com/watch?v=ivRjk7T6AXw) sobre funções
            """
        )

    if opt == 'Derivada':
        st.title("Uma das regras de derivação diz que: a derivada de uma função constante é igual"
                 " a zero")
        st.number_input('Insira o valor de (x)')
        st.title("𝑓' (𝑥) = " + str(0))
        st.markdown(
            """
            Veja mais detalhes neste [video](https://www.youtube.com/watch?v=hD5OnGRZ9Do) sobre derivadas.
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