import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
from utils.sql_func import show_tables, hide_part_of_page, check_update_db, init_logging
import logging


hide_part_of_page()

# show_tables()

st.subheader("HW5. Блок SQL. Задача 3")
st.markdown(
    "- Найдите всех сотрудников из таблицы **employees** по имени **Georgi**, которые **до сих пор работают в компании** (использовать также таблицу dept_emp, поле to_date = '9999-01-01')\n"
    "- Выведите первые 5 строк, содержащих имя, фамилию, должность, дату начала работы (from_date из dept_emp), а также дату окончания работы (to_date из dept_emp)\n"
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
    test_sql = """select e.first_name, e.last_name, e.title, d.from_date, d.to_date\n
    from employees as e\n
    inner join dept_emp as d on e.emp_no = d.emp_no\n
    where e.first_name = 'Georgi' and d.to_date = '9999-01-01'\n
    limit 5"""
    logger = logging.getLogger("foobar")
    try:
        check_update_db(content=content)
        logger.info(f"Start write query: {content}")
        df = pd.read_sql(content, conn)[:80]
        st.dataframe(df)
        df_check = pd.read_sql(test_sql, conn)
        assert (
            len(set(df.columns) ^ set(df_check.columns)) == 0
        ), "Проверьте, что по итогу у вас получились те же поля (колонки), что и указаны в задании"
        assert list(df.columns) == list(
            df_check.columns
        ), "Проверьте последовательность названия полей как в задании"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert set(df.first_name) == {
            "Georgi"
        }, "Проверьте, что вы выгружаете сотрудников по имени Georgi"
        assert set(df.to_date) == {
            "9999-01-01"
        }, "Проверьте, что вы выгружаете сотрудников, которые до сих пор работают в компании"
        assert df_check.equals(df), "Проверьте, что скрипт написан согласно заданию"
        st.success("Все верно! Ключ = 435")
    except Exception as ex:
        if ("Проверьте" in str(ex)) or ("не предусмотрено" in str(ex)):
            st.error(ex)
        else:
            st.error(
                f"Скрипт написан некорретно (неполностью, либо вовсе отсутствует). Error message: {ex}"
            )
