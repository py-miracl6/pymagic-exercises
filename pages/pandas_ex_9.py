import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 9")

df = pd.read_csv("data/hr-analysis-prediction.csv")
df1 = df[["Age", "Department", "EducationField", "DailyRate"]]
df2 = df[["Department", "EducationField"]].drop_duplicates()
df1_check = df[["Age", "Department", "EducationField", "DailyRate"]]
df2_check = df[["Department", "EducationField"]].drop_duplicates()
result_check = pd.concat([df1_check, df2_check], axis=1)

st.markdown(
    "- Представьте, что вам уже даны датасеты из задания 8 **df1** и **df2**\n"
    "- Создайте переменную **result** и присвойте ей результат конкатенации **df1** и **df2** по столбцам (axis=1)"
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
            assert df1_check.equals(df1), "Не перезаписывайте переменную df1"
            assert df2_check.equals(df2), "Не перезаписывайте переменную df2"

            # result
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert isinstance(
                loc["result"], pd.DataFrame
            ), "Проверьте тип переменной result, должен быть DataFrame"
            assert result_check.equals(
                loc["result"]
            ), "Проверьте получившийся результат в переменной result"
            st.success("Все верно! Ключ = 12")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
