import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page


hide_part_of_page()
st.subheader("HW3. Блок Python. Задача 2")
st.markdown(
    "- Создайте переменную **value** и присвойте ей список со значениями элементов с 1-го по 9-ый включительно \n"
    "- Создайте переменную **value_1** и присвойте ей элементы списка **value** с 1-го по 4-ый **индексы** (не включительно)\n"
    "- Создайте переменную **value_2** и присвойте ей последний элемент списка **value**\n"
    "- Создайте переменную **value_3** и присвойте ей два последних элемента списка **value**\n"
    "- Создайте переменную **value_4** и присвойте перевернутый список **value**"
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
    value_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value_1_check = value_check[1:4]
    value_2_check = value_check[-1]
    value_3_check = value_check[-2:]
    value_4_check = value_check[::-1]

    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            # value
            assert "value" in loc.keys(), "Проверьте название переменной value"
            value = loc["value"]
            assert isinstance(value, list), "Проверьте, что в переменной value список"
            assert value == value_check, "Проверьте значение в переменной value"
            # value_1
            assert "value_1" in loc.keys(), "Проверьте название переменной value_1"
            value_1 = loc["value_1"]
            assert value_1 == value_1_check, "Проверьте значение в переменной value_1"
            # value_2
            assert "value_2" in loc.keys(), "Проверьте название переменной value_2"
            value_2 = loc["value_2"]
            assert value_2 == value_2_check, "Проверьте значение в переменной value_2"
            # value_3
            assert "value_3" in loc.keys(), "Проверьте название переменной value_3"
            value_3 = loc["value_3"]
            assert value_3 == value_3_check, "Проверьте значение в переменной value_3"
            # value_4
            assert "value_4" in loc.keys(), "Проверьте название переменной value_4"
            value_4 = loc["value_4"]
            assert value_4 == value_4_check, "Проверьте значение в переменной value_4"
            st.success("Все верно! Ключ = 15")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
