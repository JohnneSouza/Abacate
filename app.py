import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
from src.messages import welcome
from src.pages.constants import constants
from src.pages.constants_power_x import constants_power_x
from src.pages.x_power_constant import x_power_constant
from src.pages.e_power_x import e_power_x
from src.pages.log_k import log_k
from src.pages.ln_x import ln_x
from src.pages.one_over_x import one_over_x
from src.pages.sin_x import sin_x
from src.pages.cos_x import cos_x
from src.pages.tg_x import tg_x

LOGGER = get_logger(__name__)

PAGE = OrderedDict(
    [
        ("Página Inicial", (welcome.intro, None)),
        ("𝑓 (𝑥) = k", (constants.select,
                         """
                ### Constantes

                """,),),
        (
            "𝑓 (𝑥) = 𝑥^k",
            (
                constants_power_x.select,
                """
### Constantes

""",
            ),
        ),
        (
            "𝑓 (𝑥) = k^𝑥",
            (
                x_power_constant.select,
                """
### 

""",
            ),
        ),
        (
            "𝑓 (𝑥) = e^𝑥",
            (
                e_power_x.select,
                """
### 

""",
            ),
        ),
        (
            "𝑓 (𝑥) = logK(x)",
            (
                log_k.select,
                """
### 

""",
            ),
        ),
        (
            "𝑓 (𝑥) = ln(x)",
            (
                ln_x.select,
                """
### 

""",
            ),
        ),
        (
            "𝑓 (𝑥) = 1/x",
            (
                one_over_x.select,
                """
### 

""",
            ),
        ),
        (
            "𝑓 (𝑥) = sen(x)",
            (
                sin_x.select,
                """
### 

""",
            ),
        ),
        (
            "𝑓 (𝑥) = cos(x)",
            (
                cos_x.select,
                """
### 

""",
            ),
        ),
        (
            "𝑓 (𝑥) = tan(x)",
            (
                tg_x.select,
                """
### 

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
        st.markdown("## Código fonte desta página")
        sourcelines, _ = inspect.getsourcelines(page)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()
