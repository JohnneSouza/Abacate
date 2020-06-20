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

        Matéria Cálculo - Professor Márcio Sabino
        
        Para a construção dessa aplicação foram utilizadas as seguintes ferramentas:
        - Linguagem Python -> [python.org](https://python.org/)
        - Streamlit Framework -> [streamlit.io](https://www.streamlit.io/)
        - Google Compute Engine -> [cloud.google.com](https://cloud.google.com/)  

        👈 Selecione uma opção a partir do menu ao lado para utilizar o Abacate 
        
        

        ### Quer saber como foi feito?

        - Dê uma olhadinha no código aqui no [github](https://github.com/JohnneSouza/Abacate)

    """
    )