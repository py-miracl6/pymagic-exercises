import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import pandas as pd


hide_part_of_page()
st.subheader("HW11. Блок Pandas. Задача 6")

df = pd.read_csv("data/hr-analysis-prediction.csv")
data_check = pd.read_csv("data/hr-analysis-prediction.csv")
group_check = df.fillna(df.mode().iloc[0])

st.markdown(
    "- Вам дан датасет `hr-analysis-prediction.csv`\n"
    "- Пусть ваш датасет уже записан в переменную **df** (заново прописывать не нужно)\n"
    "- Создайте переменную **fill_data**\n"
    "- Присвойте переменной **fill_data** результат заполнения датасета **df** **модой** (для каждого признака должно быть свое значение моды)\n"
    "- Так как может быть несколько мод у тех или иных признаков, возьмите моду с индексом 0 (то есть первое попавшееся значение)\n"
    "- По итогу переменная **fill_data** должна иметь тип DataFrame (по сути заполненный df)"
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
            # fill_data
            assert "fill_data" in loc.keys(), "Проверьте название переменной fill_data"
            assert isinstance(
                loc["fill_data"], pd.DataFrame
            ), "Проверьте тип переменной median_group, должен быть DataFrame"
            # st.dataframe(loc["fill_data"][:4])
            assert loc["fill_data"].isna().sum().sum() == 0, "Заполните пропуски в df"
            assert group_check.equals(
                loc["fill_data"]
            ), "Проверьте результат в переменной fill_data"

            st.success("Все верно! Ключ = 06")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
