import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
from utils.sql_func import show_tables, hide_part_of_page, check_update_db, init_logging
import logging


hide_part_of_page()
st.subheader("HW5. Блок SQL. Задача 7")
st.markdown(
    "- Вывести среднюю зарплату и название тех депаратаментов, где **среднее значение** зарплаты **больше 50000**\n"
    "- Назовите поле со средней зарплатой **avg_salary**\n"
    "- Выведите следующие поля: **название департамента - dept_name** и **размер средней зарплаты - avg_salary**\n"
    "- Не забывайте использовать таблицу dept_emp\n"
    "- Округлять в данном задании ничего не нужно\n"
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
    test_sql = """select d.dept_name, avg(s.salary) avg_salary\n
                    from dept_emp d\n
                    inner join salaries s on d.emp_no = s.emp_no\n
                    group by d.dept_name\n
                    having avg(s.salary) > 50000"""
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
        assert list(df.columns) == list(
            df_check.columns
        ), "Проверьте последовательность названия полей как в задании"
        assert (
            "dept_emp" in content.lower()
        ), "Проверьте, что вы используете таблицу dept_emp для поиска средней зарплаты в департаментах"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert (
            "group by" in content.lower()
        ), "Проверьте скрипт, возможно не хватает оператора группировки"
        assert df_check.equals(
            df
        ), "Проверьте, что скрипт написан согласно заданию, а также, что вы не округляли значения"
        st.success("Все верно! Ключ = 20")
    except Exception as ex:
        if ("Проверьте" in str(ex)) or ("не предусмотрено" in str(ex)):
            st.error(ex)
        else:
            st.error(
                f"Скрипт написан некорретно (неполностью, либо вовсе отсутствует). Error message: {ex}"
            )
