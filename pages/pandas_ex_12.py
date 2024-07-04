import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 12")

df = pd.read_csv("data/hr-analysis-prediction.csv")
data_check = pd.read_csv("data/hr-analysis-prediction.csv")

dict_check = {
    "result_val_gen": data_check.TotalWorkingYears.var(ddof=0),
    "result_val_sub": data_check.TotalWorkingYears.var(ddof=1),
    "result_std_gen": data_check.TotalWorkingYears.std(ddof=0),
    "result_std_sub": data_check.TotalWorkingYears.std(ddof=1),
    "result_iqr": (
        data_check["TotalWorkingYears"].quantile(0.75)
        - data_check["TotalWorkingYears"].quantile(0.25)
    ),
}


st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Пусть ваш датасет уже записан в переменную **df** (заново прописывать не нужно)\n"
    "- Найдите параметры характеризующие разброс для признака **TotalWorkingYears** датасета **df**:\n"
    "   - Создайте переменную **result_val_gen**, которой присвоите значение дисперсии для генеральной совокупности признака **TotalWorkingYears** (тип float)\n"
    "   - Создайте переменную **result_val_sub**, которой присвоите значение дисперсии для выборки признака **TotalWorkingYears** (тип float)\n"
    "   - Создайте переменную **result_std_gen**, которой присвоите значение среднеквадратического отклонения признака **TotalWorkingYears** (тип float)\n"
    "   - Создайте переменную **result_std_sub**, которой присвоите значение стандартного отклонения признака **TotalWorkingYears** (тип float)\n"
    "   - Создайте переменную **result_iqr**, которой присвоите значение IQR признака **TotalWorkingYears** (тип float)\n"
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
            for key in dict_check:
                assert key in loc.keys(), f"Проверьте название переменной {key}"
                assert isinstance(
                    loc[key], float
                ), f"Проверьте тип переменной {key}, должен быть float"
                assert (
                    loc[key] == dict_check[key]
                ), f"Проверьте получившийся результат в переменной {key}"
            st.success("Все верно! Ключ = 321")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
