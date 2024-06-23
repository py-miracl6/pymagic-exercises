import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page

hide_part_of_page()

st.subheader("HW3. Блок Python. Задача 0")
st.markdown(
    "- Создайте переменную **x** и присвойте ей значение равное 3\n"
    "- Создайте переменную **y** и присвойте ей значение равное 1.1\n"
    "- Создайте переменную **result** и запишите в нее сумму двух ранее созданных переменных **x** и **y**\n"
    "Например:"
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
    x_check = 3
    y_check = 1.1
    result_check = x_check + y_check
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            assert "x" in loc.keys(), "Проверьте название переменной x"
            assert loc["x"] == x_check, "Проверьте значение в переменной x"
            assert "y" in loc.keys(), "Проверьте название переменной y"
            assert loc["y"] == y_check, "Проверьте значение в переменной y"
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert (
                loc["result"] == result_check
            ), "Проверьте значение в переменной result"
            st.success("Все верно! Ключ = 101")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
