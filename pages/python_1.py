import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page

# from pylint import epylint as lint
# from io import StringIO

hide_part_of_page()
st.subheader("HW3. Блок Python. Задача 1")
st.markdown(
    "- Создайте переменную **x** и присвойте ей значение равное 6\n"
    "- Создайте переменную **y** и присвойте ей значение равное 2.5\n"
    "- Создайте переменную **result** и запишите в нее выражение, используя ранее объявленные переменные **x**, **y**, арифметические операторы, числа/цифры, так, чтобы по итогу значение в **result** было равно **8.75**\n"
    "Например:"
)
st.code("result = x * 2 - 2 * y / 2", language="python")

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
    x_check = 6
    y_check = 2.5
    result_check = x_check + 2 * 2 - y_check / 2
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        try:
            assert "x" in loc.keys(), "Проверьте название переменной x"
            assert loc["x"] == x_check, "Проверьте значение в переменной x"
            assert "y" in loc.keys(), "Проверьте название переменной y"
            assert loc["y"] == y_check, "Проверьте значение в переменной y"
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert (
                loc["result"] == result_check
            ), "Проверьте значение в переменной result"
            st.success("Все верно! Ключ = 51")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
