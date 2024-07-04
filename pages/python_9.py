import streamlit as st
from streamlit_ace import st_ace
from typing import Any, Union, List
from utils.help_func import stdoutIO, hide_part_of_page
import inspect


hide_part_of_page()
st.subheader("HW4. Блок Python. Задача 5")
st.markdown(
    "- Пусть класс **Number** вам уже дан со всеми атрибутами (из задания 3), заново его определять не нужно\n"
    "- <span style='color:red;'>Скопируйте код, при помощи которого вы создали класс **Math** в 4 задании</span>, но теперь добавьте к нему:\n"
    "   - Метод **summation** - должен быть **статическим и инкапсулированным** (недоступным ИЗВНЕ по одной черте)\n"
    "   - Метод **summation** - должен принимать на вход **value** - объект типа list и **возвращать сумму элементов**. Предусмотреть исключения **TRY-EXCEPT**, **при ошибке не должно НИЧЕГО возвращаться**\n"
    "   - Метод **average** - должен находить среднее значение списка **value_lst**, который вы унаследовали из **Number**\n"
    "   - Чтобы найти среднее значение используйте также метод **summation**. Предусмотреть исключения **TRY-EXCEPT**, **при ошибке не должно НИЧЕГО возвращаться**\n"
    "- Не забывайте про **DOCSTRING**, а также **TYPE HINTS**\n"
    "- После определения класса, определите объект класса (экземпляра класса), закрепив за ним название переменной **math**\n"
    "- В качестве аргументов подайте значения **value_lst = [2, 3, 4]**, **number = 2**\n"
    "- Переменной **result_1** присвойте вызов метода **average** экземпляра класса **math**\n"
    "- Переменной **result_2** присвойте вызов метода **summation** экземпляра класса **math**, куда подадите на вход атрибут **value_lst** экземпляра класса **math**\n"
    "\n**Пример:**",
    unsafe_allow_html=True,
)
st.code(
    "math = Math(value_lst = [2, 3, 4], number = 2)\n"
    "result_1 = math.average()\n"
    "result_2 = math._summation(math.value_lst)",
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


def test_math(data):
    # Math
    assert "Math" in data.keys(), "Проверьте название класса Math"
    assert isinstance(data["Math"].__doc__, str), "Напишите docstring для Math"

    # __init__
    assert "__init__" in data["Math"].__dict__, "Проверьте наличие метода __init__()"
    assert isinstance(
        data["Math"].__init__.__doc__, str
    ), "Напишите docstring для метода _ _ init _ _()"
    assert (
        "value_lst" in data["Math"]([2, 3], 1).__dict__
    ), "Проверьте, что в _ _ init _ _() подаете value_lst"

    assert (
        "number" in data["Math"]([2, 3], 1).__dict__
    ), "Проверьте, что в _ _ init _ _() подаете number"
    assert (
        len(data["Math"].__dict__["__init__"].__annotations__.keys()) == 3
    ), "Добавьте type hints в методе _ _ init _ _() для value_lst, number и возвращаемого значения"
    assert data["Math"].__dict__["__init__"].__annotations__["value_lst"] in [
        list,
        List[Any],
    ], "Проверьте тип type hints для value_lst в методе _ _ init _ _()"
    assert (
        data["Math"].__dict__["__init__"].__annotations__["number"] == int
    ), "Проверьте тип type hints для number в методе _ _ init _ _()"
    assert (
        data["Math"].__dict__["__init__"].__annotations__["return"] is None
    ), "Проверьте тип type hints для возвращаемого значения в методе _ _ init _ _(), должен быть None"

    # multi
    assert "multi" in data["Math"].__dict__, "Проверьте наличие метода multi()"
    assert isinstance(
        data["Math"].multi.__doc__, str
    ), "Напишите docstring для метода multi()"
    assert (
        len(data["Math"].__dict__["multi"].__annotations__.keys()) == 1
    ), "Проверьте, что метод multi() не принимает параметров (кроме self), а также type hints для возвращаемого значения"
    assert data["Math"].__dict__["multi"].__annotations__["return"] in [
        Union[None, list],
        Union[list, None],
        Union[None, List[Any]],
        Union[List[Any], None],
    ], "Проверьте тип type hints для возвращаемого значения в методе multi() (подсказка Union[None, ....])"


if content:
    st.markdown("### Результат")
    # st.subheader("Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        # exec(content, globals(), loc)
        try:
            test_math(loc)

            # summation
            assert (
                "_summation" in loc["Math"].__dict__
            ), "Проверьте наличие метода _summation()"
            assert isinstance(
                inspect.getattr_static(loc["Math"], "_summation"), staticmethod
            ), "Проверьте, что метод _summation() статический"
            assert isinstance(
                loc["Math"]._summation.__doc__, str
            ), "Напишите docstring для метода _summation()"
            assert (
                len(loc["Math"]._summation.__annotations__.keys()) == 2
            ), "Проверьте, что метод _summation() принимает параметр value, а также type hints"
            assert (
                "value" in loc["Math"]._summation.__annotations__.keys()
            ), "Проверьте, что метод _summation() принимает параметр value"
            assert loc["Math"]._summation.__annotations__["value"] in [
                list,
                List[Any],
            ], "Проверьте тип type hints для value в методе _summation()"
            assert loc["Math"]._summation.__annotations__["return"] in [
                Union[int, float, None],
                Union[float, int, None],
            ], "Проверьте тип type hints для возвращаемого значения в методе _summation() (подсказка Union[..., ..., None])"

            # average
            assert (
                "average" in loc["Math"].__dict__
            ), "Проверьте наличие метода average()"
            assert isinstance(
                loc["Math"].average.__doc__, str
            ), "Напишите docstring для метода average()"
            assert (
                len(loc["Math"].__dict__["average"].__annotations__.keys()) == 1
            ), "Проверьте, что метод average() не принимает параметров (кроме self), а также type hints для возвращаемого значения"
            assert loc["Math"].__dict__["average"].__annotations__["return"] in [
                Union[float, None],
                Union[None, float],
            ], "Проверьте тип type hints для возвращаемого значения в методе average() (подсказка Union[..., ...])"

            # result
            assert "math" in loc.keys(), "Проверьте переменную math"
            assert loc["math"].value_lst == [
                2,
                3,
                4,
            ], "Проверьте передаваемые значения аргумента value_lst в Math"
            assert (
                loc["math"].number == 2
            ), "Проверьте передаваемые значения аргумента number в Math"

            assert "result_1" in loc.keys(), "Проверьте переменную result_1"
            assert loc["result_1"] == 3, "Проверьте значение в переменной result_1"
            assert "result_2" in loc.keys(), "Проверьте переменную result_2"
            assert loc["result_2"] == 9, "Проверьте значение в переменной result_2"

            # try-except
            # multi
            try:
                assert (
                    loc["Math"](["str", 1], 3.4).multi() is None
                ), "Проверьте, что в блоке except используется простой вывод сообщения об ошибке"
            except Exception as ex:
                if "что в блоке except" in str(ex):
                    st.error(ex)
                else:
                    st.error("Проверьте наличие блока try-except в методе multi()")
            # _summation
            try:
                assert (
                    loc["Math"]._summation([1, "hh"]) is None
                ), "Проверьте, что в блоке except используется простой вывод сообщения об ошибке"
            except Exception as ex:
                if "что в блоке except" in str(ex):
                    st.error(ex)
                else:
                    st.error("Проверьте наличие блока try-except в методе _summation()")
            # average
            try:
                assert (
                    loc["Math"]([1, "hh"], 4).average() is None
                ), "Проверьте, что в блоке except используется простой вывод сообщения об ошибке"
                st.success("Все верно! Ключ = 11")
            except Exception as ex:
                if "что в блоке except" in str(ex):
                    st.error(ex)
                else:
                    st.error("Проверьте наличие блока try-except в методе average()")

        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
