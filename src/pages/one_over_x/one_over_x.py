import streamlit as st


def select():
    st.title("Escolha uma opção abaixo")

    opt = st.radio("", ('Função', 'Derivada', 'Integral Definida'))

    if opt == 'Função':
        x_var = st.number_input('Insira o valor de 𝑥')
        st.title("Se 𝑥 = {}".format(x_var))
        if x_var == 0:
            st.markdown(
                """
                Não é possível realizar divisão por 0 (zero) 
                veja os detalhes neste [video](https://www.youtube.com/watch?v=J2z5uzqxJNU) sobre divisão por 0.
                """)
        try:
            st.title("𝑓 (𝑥) = 1/{}".format(x_var))
            st.title("𝑓 ({}) = {:.4f}".format(x_var, 1/x_var))
        except:
            st.title("Tente trocar o valor de X")

    if opt == 'Derivada':
        x_var = st.number_input('Insira o valor de 𝑥')
        st.title("Se 𝑥 = {}".format(x_var))
        if x_var == 0:
            st.markdown(
                """
                Não é possível realizar divisão por 0 (zero) 
                veja os detalhes neste [video](https://www.youtube.com/watch?v=J2z5uzqxJNU) sobre divisão por 0.
                """)
        try:
            st.title("𝑓' (𝑥) = 1/{}".format(x_var))
            st.title("𝑓' ({}) = 1/{}^2".format(x_var, 1 / x_var))
            st.title("𝑓' ({}) = {:.4f}".format(x_var, 1 / x_var**2))
        except:
            st.title("Tente trocar o valor de X")

    if opt == 'Integral Definida':
        st.title("Integral Definida")
        st.title("Nao implementado")
