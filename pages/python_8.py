import streamlit as st
from streamlit_ace import st_ace
from typing import Any, Union, List
from utils.help_func import stdoutIO, hide_part_of_page
import inspect


hide_part_of_page()
st.subheader("HW4. Блок Python. Задача 4")
st.markdown(
    "- <span style='color:red;'>**СКОПИРУЙТЕ ИТОГОВОЕ РЕШЕНИЕ ДЛЯ СЛЕДУЮЩЕГО ЗАДАНИЯ**</span>\n"
    "- Пусть класс **Number** вам уже дан со всеми атрибутами (из прошлого задания), заново его определять не нужно\n"
    "- Определите класс  **Math**, который будет являться дочерним классом от **Number** и унаследует все атрибуты данного класса\n"
    "- Определите дополнительно в классе **Math** свойства:\n"
    "   - Динамическую переменную **number** - число (тип int)\n"
    "   - Метод **multi** - должен возвращать список (тип list), который сформирован путем умножения **number** на каждое из значений списка **value_lst** (унаследован из Number)\n"
    "   - В методе **multi** должно быть предусмотрено исключение **TRY-EXCEPT** на случай, если **number** будет умножен на нерелевантный тип данных, **при ошибке не должно НИЧЕГО возвращаться**\n"
    "- Не забывайте про **DOCSTRING**, а также **TYPE HINTS**\n"
    "- После определения класса, определите объект класса (экземпляра класса), закрепив за ним название переменной **math**\n"
    "- В качестве аргументов подайте значения **value_lst = [1, 2, 3]**, **number = 3**\n"
    "- Переменной **result** присвойте вызов метода **multi** экземпляра класса **math**\n"
    "\n**Пример:**",
    unsafe_allow_html=True,
)
st.code(
    "math = Math(value_lst = [1, 2, 3], number = 3)\n" "result = math.multi()",
    language="python",
)


class Number:
    """Класс для определения списка со различными значениями"""

    def __init__(self, value_lst: list) -> None:
        """Инициализация списка"""
        self.value_lst = value_lst

    def show(self) -> None:
        """Вывод значений"""
        print(self.value_lst)


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
    # st.subheader("Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            # test_number(loc)

            # Math
            assert "Math" in loc.keys(), "Проверьте название класса Math"
            assert isinstance(loc["Math"].__doc__, str), "Напишите docstring для Math"

            # __init__
            assert (
                "__init__" in loc["Math"].__dict__
            ), "Проверьте наличие метода __init__()"
            assert isinstance(
                loc["Math"].__init__.__doc__, str
            ), "Напишите docstring для метода _ _ init _ _()"
            assert (
                "value_lst" in loc["Math"]([2, 3], 1).__dict__
            ), "Проверьте, что в _ _ init _ _() подаете value_lst"

            assert (
                "number" in loc["Math"]([2, 3], 1).__dict__
            ), "Проверьте, что в _ _ init _ _() подаете number"
            assert (
                len(loc["Math"].__dict__["__init__"].__annotations__.keys()) == 3
            ), "Добавьте type hints в методе _ _ init _ _() для value_lst, number и возвращаемого значения"
            assert loc["Math"].__dict__["__init__"].__annotations__["value_lst"] in [
                list,
                List[Any],
            ], "Проверьте тип type hints для value_lst в методе _ _ init _ _()"
            assert (
                loc["Math"].__dict__["__init__"].__annotations__["number"] == int
            ), "Проверьте тип type hints для number в методе _ _ init _ _()"
            assert (
                loc["Math"].__dict__["__init__"].__annotations__["return"] is None
            ), "Проверьте тип type hints для возвращаемого значения в методе _ _ init _ _(), должен быть None"

            # multi
            assert "multi" in loc["Math"].__dict__, "Проверьте наличие метода multi()"
            assert isinstance(
                loc["Math"].multi.__doc__, str
            ), "Напишите docstring для метода multi()"
            assert (
                len(loc["Math"].__dict__["multi"].__annotations__.keys()) == 1
            ), "Проверьте, что метод multi() не принимает параметров (кроме self), а также type hints для возвращаемого значения"
            assert loc["Math"].__dict__["multi"].__annotations__["return"] in [
                Union[None, list],
                Union[list, None],
                Union[None, List[Any]],
                Union[List[Any], None],
            ], "Проверьте тип type hints для возвращаемого значения в методе multi() (подсказка Union[None, ....])"

            # result
            assert "math" in loc.keys(), "Проверьте переменную math"
            assert "result" in loc.keys(), "Проверьте переменную result"

            assert loc["math"].value_lst == [
                1,
                2,
                3,
            ], "Проверьте передаваемые значения аргумента value_lst в Math"
            assert (
                loc["math"].number == 3
            ), "Проверьте передаваемые значения аргумента number в Math"
            assert loc["result"] == [3, 6, 9], "Проверьте значения в переменной result"

            # try-except
            try:
                assert (
                    loc["Math"](["str", 1], 3.4).multi() is None
                ), "Проверьте, что в блоке except используется простой вывод сообщения об ошибке"
                st.success("Все верно! Ключ = 99")
            except Exception as ex:
                if "что в блоке except" in str(ex):
                    st.error(ex)
                else:
                    st.error("Проверьте наличие блока try-except в методе multi()")
            # st.success("Все верно! Ключ = 92")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
