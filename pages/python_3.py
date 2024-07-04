import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page


hide_part_of_page()
st.subheader("HW3. Блок Python. Задача 3")
st.markdown(
    "- Создайте переменную **value** и присвойте ей список, включающий три любых значения\n"
    "- Добавьте в конец списка строку **'это строка'**"
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
    st.subheader("Результат")
    value_check = [1, 2, 3]
    value_check_append = value_check.copy()
    value_check_append.append("это строка")

    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            assert "value" in loc.keys(), "Проверьте название переменной value"
            value = loc["value"]
            assert isinstance(value, list), "Проверьте, что в переменной value список"
            assert len(value[:-1]) == len(
                value_check
            ), "Проверьте кол-во значений в переменной value"
            assert (
                value[-1] == value_check_append[-1]
            ), "Проверьте, что вы добавили в список элемент со значением 'это строка'"
            st.success("Все верно! Ключ = 68")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
