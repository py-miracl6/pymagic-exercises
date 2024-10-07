import streamlit as st
from streamlit_ace import st_ace
from typing import Any, Union, List
from utils.help_func import stdoutIO, hide_part_of_page


hide_part_of_page()
st.subheader("HW4. Блок Python. Задача 2")
st.markdown(
    "- Создайте функцию с *неизвестным количеством неименованных аргументов* и назовите ее **adding_str_values**, в качестве названия неименнованных аргументов примите **args**\n"
    "- Неименованные аргументы могут быть любого типа (подсказка Any)\n"
    "- Если аргумент типа **str**, то необходимо внутри функции реализовать добавление его в список (подсказка List comprehension)\n"
    "- Функция должна возвращать **итоговый список** со всеми аргументами типа str\n"
    "- Не забывайте про **TYPE HINTS**\n"
    "- Создайте переменную **result** и присвойте ей вызов функции **adding_str_values**, подав следующие значения:"
)
st.code('"строка", 1, 3.5, "значение", True, {1: 45, 9: [1, 3]}', language="python")

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


def test_adding_str_values(*args):
    """Add values"""
    return [i for i in args if isinstance(i, str)]


result_check = test_adding_str_values(
    "строка", 1, 3.5, "значение", True, {1: 45, 9: [1, 3]}
)
result_check_two = test_adding_str_values("строка", 1, 3.5)

if content:
    st.markdown("### Результат")
    # st.subheader("Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            assert (
                "adding_str_values" in loc.keys()
            ), "Проверьте название функции adding_str_values()"
            assert (
                len(loc["adding_str_values"].__annotations__.keys()) == 2
            ), "Добавьте type hints для args и возвращаемого значения"
            assert (
                loc["adding_str_values"].__annotations__["args"] == Any
            ), "Проверьте тип type hints для value_1"
            assert loc["adding_str_values"].__annotations__["return"] in [
                list,
                List[str],
                list[str],
            ], "Проверьте тип type hints для возвращаемого значения"
            assert "result" in loc.keys(), "Проверьте переменную result"
            assert (
                loc["adding_str_values"]("строка", 1, 3.5) == result_check_two
            ), "Проверьте функцию adding_str_values на то, что она добавляет элементы типа str в список и возвращает его"
            assert (
                loc["result"] == result_check
            ), "Проверьте значение в переменной result"
            st.success("Все верно! Ключ = 92")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
