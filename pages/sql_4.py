import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
from utils.sql_func import show_tables, hide_part_of_page, check_update_db, init_logging
import logging


hide_part_of_page()

st.subheader("HW5. Блок SQL. Задача 4")
st.markdown(
    "- Вывести **ТОП-2** заплаты в каждом департаменте, используя **оконные функции**\n"
    "- Выведите поля с названием **департамета и размером зарплаты**\n"
    "- Используйте сортировку по убыванию в самой оконной функции, а также JOIN для соединения таблиц\n"
    "- Если в департаменте несколько похожих зарплат, то учитывать только уникальные значения!\n"
    "- Для большего удобства используйте **обобщенное табличное выражение или CTE** (WITH)\n"
    "- Будьте внимательны, так как зарплаты у сотрудников могут быть одинаковыми в одном и том же депаратаменте, использование некоторых оконных функций может дать неккоректный результат\n"
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
    test_sql = """with max_salary as (\n
                    select d.dept_name, s.salary,\n
                    DENSE_RANK() OVER (PARTITION BY d.dept_name ORDER BY s.salary desc) as rn\n
                    from dept_emp d\n
                    inner join salaries s on d.emp_no = s.emp_no
                    )\n
                select dept_name, salary\n
                from max_salary\n
                where rn <= 2"""
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
            "over" in content.lower()
        ), "Проверьте, что вы используете оконную функцию"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert df_check.equals(df), "Проверьте, что скрипт написан согласно заданию"
        st.success("Все верно! Ключ = 76")
    except Exception as ex:
        if ("Проверьте" in str(ex)) or ("не предусмотрено" in str(ex)):
            st.error(ex)
        else:
            st.error(
                f"Скрипт написан некорретно (неполностью, либо вовсе отсутствует). Error message: {ex}"
            )
