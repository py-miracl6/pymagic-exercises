import streamlit as st
import pandas as pd
from sqlite3 import connect
import logging
from streamlit import runtime
from streamlit.runtime.scriptrunner import get_script_run_ctx


def show_tables(url_db: str = "data/EmployeeSQL.db"):
    col1, col2, col3, col4 = st.columns(4)
    conn = connect(url_db)

    with col1:
        df = pd.read_sql("SELECT * FROM employees limit 4", conn)
        st.write("Table - **employees**")
        st.dataframe(df)

    with col2:
        df = pd.read_sql("SELECT * FROM dept_emp limit 4", conn)
        st.write("Table - **dept_emp**")
        st.dataframe(df)

    with col3:
        df = pd.read_sql("SELECT * FROM dept_manager limit 4", conn)
        st.write("Table - **dept_manager**")
        st.dataframe(df)

    with col4:
        df = pd.read_sql("SELECT * FROM salaries limit 4", conn)
        st.write("Table - **salaries**")
        st.dataframe(df)


def hide_part_of_page():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        [data-testid="collapsedControl"] {
        display: none
        }
        [kind="header"] {visibility: hidden;}
        [data-testid="stHeader"] {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def check_update_db(content):
    assert (
        len(content.lower().split('from ')[1].split('where')[0].split('join')[0].split(',')) <= 1
    ), "В FROM не может быть указано две таблицы"
    assert (
        "create" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"
    assert (
        "alter" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"
    assert (
        "delete" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"
    assert (
        "update" not in content.lower()
    ), "В данном функционале не предусмотрено изменение и создание таблиц"


def get_remote_ip() -> str:
    """Get remote ip."""

    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None

        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception as e:
        return None

    return session_info.request.remote_ip

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.user_ip = get_remote_ip()
        return super().filter(record)

def init_logging():
    # Make sure to instanciate the logger only once
    # otherwise, it will create a StreamHandler at every run
    # and duplicate the messages

    # create a custom logger
    logger = logging.getLogger("foobar")
    if logger.handlers:  # logger is already setup, don't setup again
        return
    logger.propagate = False
    logger.setLevel(logging.INFO)
    # in the formatter, use the variable "user_ip"
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s [user_ip=%(user_ip)s] - %(message)s")
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.addFilter(ContextFilter())
    handler.setFormatter(formatter)
    logger.addHandler(handler)
