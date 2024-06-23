import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 11")

df = pd.read_csv("data/hr-analysis-prediction.csv")
data_check = pd.read_csv("data/hr-analysis-prediction.csv")
result_check = (
    data_check.query("Education == 3 or Education == 4")["Department"]
    .value_counts(normalize=True)
    .to_frame("percent")
)


st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Пусть ваш датасет уже записан в переменную **df** (заново прописывать не нужно)\n"
    "- Создайте переменную **result**, которой присвоите датасет подсчитанный следующим образом:\n"
    "   - Необходимо подсчитать количество сотрудников в каждом из **Департаментов** (столбец Department), которые имеют **образование** (Education): **Bachelor** (соответсвует значению = 3) ИЛИ **Master** (соответсвует значению = 4)\n"
    "   - Далее **отнормировать** на **ОБЩЕЕ** количество людей, имеющих перечисленные степени образования (если в каком то департаменте сотрудников с таким образованием нет, то его включать не нужно)\n"
    "- Подсказка: задача решается в одну строку (value_counts). В лекции рассматривали метод, который имеет параметр для нормализации"
)
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
            assert data_check.equals(df), "Не перезаписывайте переменную df"

            # result
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert isinstance(
                loc["result"], pd.DataFrame
            ), "Проверьте тип переменной result, должен быть DataFrame"
            st.write(loc["result"])
            assert result_check.equals(
                loc["result"]
            ), "Проверьте получившийся результат в переменной result"
            st.success("Все верно! Ключ = 138")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
