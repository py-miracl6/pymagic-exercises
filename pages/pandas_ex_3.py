import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 3")

st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Пусть ваш датасет уже записан в переменную **df** (заново прописывать не нужно)\n"
    "- Создайте переменную **median_daily** и присвойте ей значение медианы признака **DailyRate** из датасета **df** (должен быть тип float)\n"
    "- Создайте переменную **median_distance** и присвойте ей значение медианы признака **DistanceFromHome** из датасета **df** (должен быть тип float)\n"
    "- Создайте переменную **median_monthly** и присвойте ей значение медианы признака **MonthlyIncome** из датасета **df** (должен быть тип float)\n"
    "- Создайте переменную **mean_income** и присвойте ей значение среднего размера зарплаты (признак **MonthlyIncome**) для работников из департамента **Human Resources**. Департамент - признак **Department** (должен быть тип float)"
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
        st.write(s.getvalue())
        try:
            assert data_check.equals(df), "Не перезаписывайте переменную df"
            # median_daily
            assert (
                "median_daily" in loc.keys()
            ), "Проверьте название переменной median_daily"
            assert isinstance(
                loc["median_daily"], float
            ), "Проверьте тип переменной median_daily"
            assert (
                loc["median_daily"] == df["DailyRate"].median()
            ), "Проверьте результат в переменной median_daily"

            # median_distance
            assert (
                "median_distance" in loc.keys()
            ), "Проверьте название переменной median_distance"
            assert isinstance(
                loc["median_distance"], float
            ), "Проверьте тип переменной median_daily"
            assert (
                loc["median_distance"] == df["DistanceFromHome"].median()
            ), "Проверьте результат в переменной median_distance"

            # median_monthly
            assert (
                "median_monthly" in loc.keys()
            ), "Проверьте название переменной median_monthly"
            assert isinstance(
                loc["median_monthly"], float
            ), "Проверьте тип переменной median_monthly"
            assert (
                loc["median_monthly"] == df["MonthlyIncome"].median()
            ), "Проверьте результат в переменной median_monthly"

            # mean_income
            assert (
                "mean_income" in loc.keys()
            ), "Проверьте название переменной mean_income"
            assert isinstance(
                loc["mean_income"], float
            ), "Проверьте тип переменной mean_income"
            assert (
                loc["mean_income"]
                == df.query("Department=='Human Resources'")["MonthlyIncome"].mean()
            ), "Проверьте результат в переменной mean_income"

            st.success("Все верно! Ключ = 06")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
