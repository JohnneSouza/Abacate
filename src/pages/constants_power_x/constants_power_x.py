import streamlit as st

# TODO TROCAR LINK DOS VIDEOS
def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        x_var = st.number_input('Insira o valor de (x)')
        k_var = st.number_input('Insira o valor de (k)')

        st.title("𝑓 (𝑥) = x^k")
        st.title("f (𝑥) = {: .2f}".format(x_var**k_var))

        st.markdown(
            """
            Veja mais detalhes neste [video](https://www.youtube.com/watch?v=ivRjk7T6AXw) sobre funções
            """
        )

    if opt == 'Derivada':
        st.title("Derivada utilizando a regra do tombo")
        x_var = st.number_input('Insira o valor de (𝑥)')
        k_var = st.number_input('Insira o valor de (k)')

        if k_var != 0 or x_var != 0:
            try:
                st.title("Se 𝑥 = {} e k = {}".format(x_var, k_var))
                st.title("𝑓' (𝑥) = {}*{}^({}-1)".format("k", "𝑥", "k"))
                st.title("𝑓' (𝑥) = {}*{}^({})".format(k_var, x_var, k_var - 1))
                st.title("𝑓' (𝑥) = {:.2f}".format(k_var*x_var**(k_var-1)))
            except:
                st.title("O valor atual é invalido, tente trocar o valor de X ou K")

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