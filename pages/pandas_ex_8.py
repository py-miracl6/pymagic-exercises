import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 8")

df = pd.read_csv("data/hr-analysis-prediction.csv")
data_check = pd.read_csv("data/hr-analysis-prediction.csv")
df1_check = df[["Age", "Department", "EducationField", "DailyRate"]]
df2_check = df[["Department", "EducationField"]].drop_duplicates()
result_check = pd.merge(df1_check, df2_check, on=["EducationField", "Department"])

st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Пусть ваш датасет уже записан в переменную **df** (заново прописывать не нужно)\n"
    "- Создайте переменную **df1**, которой присвоите датасет **df** со столбцами **Age**, **Department**, **EducationField** и **DailyRate** (должен быть тип DataFrame)\n"
    "- Создайте переменную **df2**, которой присвоите датасет **df** со столбцами **Department** и **EducationField** (должен быть тип DataFrame), также в **df2 необходимо УДАЛИТЬ дубли**\n"
    "- Создайте переменную **result** и присвойте ей результат объединения **df1** и **df2** по столбцам **Department и EducationField** при помощи `pandas.merge()` (используйте тип соединения **inner**)\n"
    "- Удаление дублей: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html\n"
    "Пример:\n"
)
st.code("df1 = # ваш код\ndf2 = # ваш код\nresult = # ваш код", language="python")

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

            # df1
            assert "df1" in loc.keys(), "Проверьте название переменной df1"
            assert isinstance(
                loc["df1"], pd.DataFrame
            ), "Проверьте тип переменной df1, должен быть DataFrame"
            assert df1_check.equals(loc["df1"]), "Проверьте значения в df1"

            # df2
            assert "df2" in loc.keys(), "Проверьте название переменной df2"
            assert isinstance(
                loc["df2"], pd.DataFrame
            ), "Проверьте тип переменной df2, должен быть DataFrame"
            assert df2_check.equals(loc["df2"]), "Проверьте значения в df2"

            # result
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert isinstance(
                loc["result"], pd.DataFrame
            ), "Проверьте тип переменной result, должен быть DataFrame"
            assert result_check.equals(
                loc["result"]
            ), "Проверьте получившийся результат в переменной result"
            st.success("Все верно! Ключ = 0")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
