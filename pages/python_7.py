import streamlit as st
from streamlit_ace import st_ace
from typing import Any, Union, List
from utils.help_func import stdoutIO, hide_part_of_page
import inspect


hide_part_of_page()
st.subheader("HW4. Блок Python. Задача 3")

st.markdown(
    "- <span style='color:red;'>**СКОПИРУЙТЕ ИТОГОВОЕ РЕШЕНИЕ ДЛЯ СЛЕДУЮЩЕГО ЗАДАНИЯ**</span>\n"
    "- Определите класс **Number**, в котором определите свойства:\n"
    "   - Динамическую переменную **value_lst** - это список с различными типами данных (укажите в аннотации типов list)\n"
    "   - Метод **show**, который выводит значениие **value_lst** (подсказка: используйте self)\n"
    "- После определения класса, определите объект класса (экземпляра класса), закрепив за ним название переменной **result**\n"
    "- В качестве аргумента подайте список [1, 2, 3]\n"
    "- Далее вызовите метод **show** экземпляра класса **result**\n"
    "- Не забывайте про **DOCSTRING**, а также **TYPE HINTS**\n"
    "\n**Пример:**",
    unsafe_allow_html=True,
)
st.code("result = Number(value_lst = [1, 2, 3])\n" "result.show()", language="python")

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


class Number_check:
    def __init__(self, value_lst: list) -> None:
        self.value_lst = value_lst


result_check = Number_check([1, 2, 3])


if content:
    st.markdown("### Результат")
    # st.subheader("Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            # Number
            assert "Number" in loc.keys(), "Проверьте название класса Number"
            assert isinstance(
                loc["Number"].__doc__, str
            ), "Напишите docstring для Number"

            # __init__
            assert (
                "__init__" in loc["Number"].__dict__
            ), "Проверьте наличие метода __init__()"
            assert isinstance(
                loc["Number"].__init__.__doc__, str
            ), "Напишите docstring для метода _ _ init _ _()"
            assert (
                "value_lst" in loc["Number"](1).__dict__
            ), "Проверьте, что в _ _ init _ _() подаете value_lst"
            assert (
                len(loc["Number"].__dict__["__init__"].__annotations__.keys()) == 2
            ), "Добавьте type hints для value_lst и возвращаемого значения в методе _ _ init _ _()"
            assert loc["Number"].__dict__["__init__"].__annotations__["value_lst"] in [
                list,
                List[Any],
                List,
            ], "Проверьте тип type hints для value_lst в методе _ _ init _ _()"
            assert (
                loc["Number"].__dict__["__init__"].__annotations__["return"] is None
            ), "Проверьте тип type hints для возвращаемого значения в методе _ _ init _ _(), должен быть None"

            # show
            assert "show" in loc["Number"].__dict__, "Проверьте наличие метода show()"
            assert isinstance(
                loc["Number"].show.__doc__, str
            ), "Напишите docstring для метода show()"
            assert not isinstance(
                inspect.getattr_static(loc["Number"], "show"), staticmethod
            ), "Метод show() не должен быть статическим"
            assert (
                len(loc["Number"].show.__annotations__.keys()) == 1
            ), "Проверьте, что show() ничего не принимает на вход кроме self, а также type hints для возвращаемого значения"
            assert (
                loc["Number"].show.__annotations__["return"] is None
            ), "Проверьте тип type hints для возвращаемого значения в методе show() (должно быть None, так как ничего не возвращает)"

            # result
            assert "result" in loc.keys(), "Проверьте переменную result"
            assert loc["result"].value_lst == [
                1,
                2,
                3,
            ], "Проверьте передаваемые значения аргумента value_lst в Number"
            assert (
                s.getvalue().find("[1, 2, 3]") > -1
            ), "Вызовите метод show() экземпляра класса result"
            st.success("Все верно! Ключ = 92")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
