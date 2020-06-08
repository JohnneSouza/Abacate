import streamlit as st


def intro():
    st.sidebar.success("Selecione uma opção acima.")

    st.markdown(
        """
        Abacus Calculator Tech
        
        Abacate é uma aplicação desenvolvida durante o curso
        de Análise e Desenvolvimento de Sistemas na FATEC
        Athur de Azevedo 
        [Site FATECMM](http://fatecmm.edu.br/) 

        Matéria Cálculo

        👈 Selecione uma opção a partir do menu ao lado para utilizar o Abacate 
        
        

        ### Quer saber como feito?

        - Dê uma olhadinha no código aqui no [github](https://github.com/JohnneSouza/Abacate)

    """
    )