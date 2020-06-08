import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
from src.messages import welcome
from src.pages.constants import constants

LOGGER = get_logger(__name__)

# Dictionary of
# demo_name -> (demo_function, demo_description)
PAGE = OrderedDict(
    [
        ("Página Inicial", (welcome.intro, None)),
        (
            "𝑓(𝑥) = k",
            (
                constants.select,
                """
### Função constante
Em matemática, uma função constante é uma função cujo valor (de saída) é o mesmo para todos os valores de entrada
""",
            ),
        ),
    ]
)


def run():
    page_selected = st.sidebar.selectbox("Escolha uma opção no menu abaixo", list(PAGE.keys()), 0)
    page = PAGE[page_selected][0]

    if page_selected == "Página Inicial":
        show_code = False
        st.write("#  🥑 Bem vindo ao Abacate! 👋")
    else:
        show_code = st.sidebar.checkbox("Exibir Código", False)
        st.markdown("# %s" % page_selected)
        description = PAGE[page_selected][1]
        if description:
            st.write(description)
        for i in range(10):
            st.empty()

    page()

    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(page)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()
