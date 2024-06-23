import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 2")

st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Пусть ваш датасет уже записан в переменную **df** из прошлого задания (заново прописывать не нужно)\n"
    "- Создайте переменную **result_1** и присвойте ей использование метода из pandas с выводом информации о датасете **df**: типы данных по каждому столбцу, а также пропуски при помощи **ОДНОГО метода**.\n"
    "- Создайте переменную **result_2** и присвойте ей использование метода из pandas с выводом информации только о размере датасете **df** (должен быть тип tuple)"
)

df = pd.read_csv("data/hr-analysis-prediction.csv")
data_check = pd.read_csv("data/hr-analysis-prediction.csv")

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
        # st.write(s.getvalue())
        try:
            assert data_check.equals(df), "Не перезаписывайте переменную df"
            assert "result_1" in loc.keys(), "Проверьте название переменной result_1"
            assert (
                loc["result_1"] == df.info()
            ), "Проверьте результат в переменной result_1"

            assert "result_2" in loc.keys(), "Проверьте название переменной result_2"
            assert isinstance(loc["result_2"], tuple), "Проверьте тип переменной df"
            assert (
                loc["result_2"] == df.shape
            ), "Проверьте результат в переменной result_2"
            st.success("Все верно! Ключ = 765")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
