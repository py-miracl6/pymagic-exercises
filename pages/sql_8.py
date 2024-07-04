import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
from utils.sql_func import show_tables, hide_part_of_page, check_update_db, init_logging
import logging


hide_part_of_page()
st.subheader("HW5. Блок SQL. Задача 8")
st.markdown(
    "- Вывести ТОЛЬКО среднюю зарплату по ВСЕМ сотрудникам и **округлить ее до двух знаков** после запятой при помощи ROUND()\n"
    "- Назовите поле со средней зарплатой **avg_salary**\n"
    "- Оконные функции использовать в этом задании не нужно!\n"
    "\n**Примечание**: вам уже даны таблицы, их импортировать не нужно, также можно выводить\n"
    "таблицу только до 80 строк при тестировании скрипта"
)
show_tables()

loc = {}
content = st_ace(
    placeholder="Ваш скрипт",
    language="sqlserver",
    theme="xcode",
    keybinding="vscode",
    show_gutter=True,
    min_lines=10,
    key="ace",
)

if content:
    init_logging()
    conn = connect("data/EmployeeSQL.db")
    st.markdown("### Результат")
    test_sql = """SELECT round(AVG(salary), 2) as avg_salary
                    FROM salaries"""
    logger = logging.getLogger("foobar")
    try:
        check_update_db(content=content)
        logger.info(f"Start write query: {content}")
        df = pd.read_sql(content, conn)[:80]
        st.dataframe(df)
        df_check = pd.read_sql(test_sql, conn)

        assert (
            "over" not in content.lower()
        ), "Проверьте, что вы не используете в запросе оконные функции"
        assert (
            "avg_salary" in content.lower()
        ), "Проверьте, что название поля со средней зарплатой - avg_salary"
        assert (
            len(set(df.columns) ^ set(df_check.columns)) == 0
        ), "Проверьте, что по итогу у вас получились те же поля (колонки), что в задании"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert (
            round(df["avg_salary"][0]) == 52971
        ), "Проверьте, что скрипт написан согласно заданию"
        assert (
            df["avg_salary"][0] == 52970.73
        ), "Проверьте на сколько знаков после запятой вы округлили значение"
        assert df_check.equals(df), "Проверьте, что скрипт написан согласно заданию"
        st.success("Все верно! Ключ = 01")
    except Exception as ex:
        if ("Проверьте" in str(ex)) or ("не предусмотрено" in str(ex)):
            st.error(ex)
        else:
            st.error(
                f"Скрипт написан некорретно (неполностью, либо вовсе отсутствует). Error message: {ex}"
            )
