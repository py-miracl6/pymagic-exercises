import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
import re
from utils.sql_func import show_tables, hide_part_of_page, check_update_db, init_logging
import logging


hide_part_of_page()
st.subheader("HW5. Блок SQL. Задача 10")
st.markdown(
    "- Найдите **количество уникальных сотрудников** в каждом **департаменте** в разрезе **должности**\n"
    "   - У вас должны получится следующие поля: dept_name, title, count_emp\n"
    "- Оконные функции использовать в этом задании не нужно!\n"
    "- Назовите поле, где будет указано кол-во уникальных сотрудников **count_emp**\n"
    "**Примечание**: вам уже даны таблицы, их импортировать не нужно, также можно выводить\n"
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
    test_sql = """select d.dept_name, e.title, count(e.emp_no) as count_emp\n
                    from employees e\n
                    inner join dept_emp d on e.emp_no = d.emp_no\n
                    GROUP BY d.dept_name, e.title"""
    test_sql_2 = """select d.dept_name, e.title, count(e.emp_no) as count_emp\n
                    from employees e\n
                    inner join dept_emp d on e.emp_no = d.emp_no\n
                    GROUP BY e.title, d.dept_name"""
    logger = logging.getLogger("foobar")
    try:
        check_update_db(content=content)
        logger.info(f"Start write query: {content}")
        df = pd.read_sql(content, conn)[:80]
        st.dataframe(df)
        df_check = pd.read_sql(test_sql, conn)
        df_check2 = pd.read_sql(test_sql_2, conn)

        assert (
            "over" not in content.lower()
        ), "Проверьте, что вы не используете в запросе оконные функции"
        assert "order" not in content.lower(), "В задании не предусмотрена сортировка"
        assert (
            "employees" in content.lower()
        ), "Проверьте, что вы используете таблицу employees для подсчета кол-ва уникальных сотрудников"
        assert (
            "dept_emp" in content.lower()
        ), "Проверьте, что вы используете таблицу dept_emp для подсчета кол-ва уникальных сотрудников"
        assert (
            "count_emp" in content.lower()
        ), "Проверьте, что вы использовали название поля count_emp"
        assert (
            len(set(df.columns) ^ set(df_check.columns)) == 0
        ), "Проверьте, что по итогу у вас получились те же поля (колонки), что в задании"
        assert list(df.columns) == list(
            df_check.columns
        ), "Проверьте последовательность названия полей как в задании"
        assert (
            "group by" in content.lower()
        ), "Проверьте, что вы группируете по полям департамент и название должности"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert (df_check.equals(df)) or (
            df_check2.equals(df)
        ), "Проверьте, что скрипт написан согласно заданию"
        st.success("Все верно! Ключ = 73")
    except Exception as ex:
        if (
            ("Проверьте" in str(ex))
            or ("не предусмотрено" in str(ex))
            or ("предусмотрена" in str(ex))
        ):
            st.error(ex)
        else:
            st.error(
                f"Скрипт написан некорретно (неполностью, либо вовсе отсутствует). Error message: {ex}"
            )
