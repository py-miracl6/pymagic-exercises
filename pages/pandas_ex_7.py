import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 7")

# df = pd.read_csv('hr-analysis-prediction.csv')
data_check = pd.read_csv("data/hr-analysis-prediction.csv")
data_check_map = pd.read_csv("data/hr-analysis-prediction.csv")
dict_education_check = {
    1: "Below College",
    2: "College",
    3: "Bachelor",
    4: "Master",
    5: "Doctor",
}
data_check_map.Education = data_check_map.Education.map(dict_education_check)

st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Импортируйте pandas и напишите краткий алиас **pd**\n"
    "- Прочитайте датасет `hr-analysis-prediction.csv` из папки `data` и запишите его в виде DataFrame в переменную **df**\n"
    "- Создайте переменную **dict_education**, куда запишите словарь (ключ тип int, значение тип str) с соответвующими значениями признака **Education**:\n"
    "   - **1** соответсвует значению **Below College**\n"
    "   - **2** соответсвует значению **College**\n"
    "   - **3** соответсвует значению **Bachelor**\n"
    "   - **4** соответсвует значению **Master**\n"
    "   - **5** соответсвует значению **Doctor**\n"
    "- Испольуя словарь **dict_education** произведите замену значений в признаке **Education**\n"
    "- Чтобы в переменной **df** в признаке **Education** произошла замена, сделайте присваивание:"
)
st.code("df.Education = # ваш код", language="python")

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

            # dict_education
            assert (
                "dict_education" in loc.keys()
            ), "Проверьте название переменной dict_education"
            assert isinstance(
                loc["dict_education"], dict
            ), "Проверьте тип переменной dict_education, должен быть dict"
            assert (
                loc["dict_education"] == dict_education_check
            ), "Проверьте значения в переменной dict_education"

            # df
            assert isinstance(
                loc["df"], pd.DataFrame
            ), "Проверьте датасет df, должен быть тип DataFrame, возможно ошибка в присваивании, либо в импорте данных"
            assert data_check_map.equals(loc["df"]), "Проверьте результат замены в df"
            st.success("Все верно! Ключ = 6")

        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
