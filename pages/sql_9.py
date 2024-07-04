import streamlit as st
from streamlit_ace import st_ace
from sqlite3 import connect
import pandas as pd
from utils.sql_func import show_tables, hide_part_of_page, check_update_db, init_logging
import logging


hide_part_of_page()
st.subheader("HW5. Блок SQL. Задача 9")
st.markdown(
    "- Вывести первые 10 строк со следующей информацией о сотрудниках:\n"
    "   - id сотрудника - emp_no\n"
    "   - Имя сотрудника\n"
    "   - Фамилия сотрудника\n"
    "   - Должность\n"
    "   - Департамент\n"
    "   - Зарплата (иметь в виду, что это число, а не строка)\n"
    "   - Дата начала работы в департаменте\n"
    "   - Дата окончания работы в департаменте\n"
    "   - Флаг того, что человек работает в данном депаратаменте, назовите поле **flg_to_date** (если стоит дата '9999-01-01', то человек продолжает работать - ставим 1, иначе 0)\n"
    "   - Флаг того, что его зарплата выше средней, назовите поле **flg_salary**, если 1 - выше или равна средней, иначе 0 (находили среднюю зарплату в прошлом задании, возьмите за значение число 52971)\n"
    "- Используйте CASE\n"
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
    test_sql = """select e.emp_no, e.first_name, e.last_name, e.title, d_e.dept_name,\n
                    s.salary, d_e.from_date, d_e.to_date,\n
                    case when (d_e.to_date = '9999-01-01') then 1 else 0 end as flg_to_date,\n
                    case when (s.salary >= 52971) then 1 else 0 end as flg_salary\n
                from employees as e\n
                left join dept_emp as d_e on e.emp_no = d_e.emp_no\n
                left join salaries as s on d_e.emp_no = s.emp_no\n
                limit 10"""
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
        assert "order" not in content.lower(), "В задании не предусмотрена сортировка"
        assert (
            "flg_to_date" in content.lower()
        ), "Проверьте, что вы использовали название поля flg_to_date"
        assert (
            "flg_salary" in content.lower()
        ), "Проверьте, что вы использовали название поля flg_salary"
        assert (
            len(set(df.columns) ^ set(df_check.columns)) == 0
        ), "Проверьте, что по итогу у вас получились те же поля (колонки), что в задании"
        assert list(df.columns) == list(
            df_check.columns
        ), "Проверьте последовательность названия полей как в задании"
        assert (
            df.shape[0] == df_check.shape[0]
        ), "Проверьте размер таблицы, получаемый в ходе выполнения скрипта"
        assert df_check.equals(df), "Проверьте, что скрипт написан согласно заданию"
        st.success("Все верно! Ключ = 00")
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
