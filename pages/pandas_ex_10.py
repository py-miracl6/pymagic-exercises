import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 10")

# df = pd.read_csv('hr-analysis-prediction.csv')
data_check = pd.read_csv("data/hr-analysis-prediction.csv")
data_check_map = pd.read_csv("data/hr-analysis-prediction.csv")
dict_attrition_check = {"Yes": 1, "No": 0}
data_check_map.Attrition = data_check_map.Attrition.map(dict_attrition_check)

st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Импортируйте pandas и напишите краткий алиас **pd**\n"
    "- Прочитайте датасет `hr-analysis-prediction.csv` из папки `data` и запишите его в виде DataFrame в переменную **df**\n"
    "- Создайте переменную **dict_attrition**, куда запишите словарь (ключ тип str, значение тип int) с соответвующими значениями признака **Attrition**:\n"
    "   - **Yes** соответсвует значению **1**\n"
    "   - **No** соответсвует значению **0**\n"
    "- Испольуя словарь **dict_attrition** произведите замену значений в признаке **Attrition**\n"
    "- Чтобы в переменной **df** в признаке **Attrition** произошла замена, сделайте присваивание:"
)
st.code("df.Attrition = # ваш код", language="python")

loc = {}
content = st_ace(
    placeholder="Ваш код",
    language="python",
    theme="chrome",
    keybinding="vscode",
    show_gutter=True,
    min_lines=10,
    key="ace",
)

if content:
    st.markdown("### Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        try:
            assert (
                "pd" in loc.keys()
            ), "Импортируйте pandas, а также используйте алиас pd"
            assert "df" in loc.keys(), "Проверьте название переменной df"

            # dict_attrition
            assert (
                "dict_attrition" in loc.keys()
            ), "Проверьте название переменной dict_attrition"
            assert isinstance(
                loc["dict_attrition"], dict
            ), "Проверьте тип переменной dict_education, должен быть dict"
            assert (
                loc["dict_attrition"] == dict_attrition_check
            ), "Проверьте значения в переменной dict_attrition"

            # df
            assert isinstance(
                loc["df"], pd.DataFrame
            ), "Проверьте датасет df, должен быть тип DataFrame, возможно ошибка в присваивании, либо в импорте данных"
            assert data_check_map.equals(loc["df"]), "Проверьте результат замены в df"
            st.success("Все верно! Ключ = 008")

        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
