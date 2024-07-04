import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import numpy as np


hide_part_of_page()
st.subheader("HW9. Блок Numpy. Задача 1")
st.markdown(
    "- Создайте переменную **array_one** и присвойте ей значение сгенерированной матрицы случайными значениями при помощи numpy **размером 6 строк на 11 столбцов** (должен быть тип переменной numpy.ndarray)\n"
    "- Создайте переменную **list_two** и присвойте ей значение сгенерированного списка случайными значениями, состоящего из **11 элементов** (должен быть тип переменной list)\n"
    "- Создайте переменную **result** и присвойте ей значение переменожения **array_one** на диагональную матрицу, созданную из списка **list_two**"
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
            # array_one
            assert "array_one" in loc.keys(), "Проверьте название переменной array_one"
            assert isinstance(
                loc["array_one"], np.ndarray
            ), "Проверьте тип переменной array_one"
            assert loc["array_one"].shape == (
                6,
                11,
            ), "Проверьте размер матрицы array_one"

            # list_two
            assert "list_two" in loc.keys(), "Проверьте название переменной array_one"
            assert isinstance(
                loc["list_two"], list
            ), "Проверьте тип переменной list_two"
            assert len(loc["list_two"]) == 11, "Проверьте размер списка list_two"

            # result
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert isinstance(
                loc["result"], np.ndarray
            ), "Проверьте тип переменной result"
            assert loc["result"].shape == (6, 11), "Проверьте размер матрицы result"
            assert np.allclose(
                loc["result"], np.dot(loc["array_one"], np.diag(loc["list_two"]))
            ), "Проверьте результат умножения матриц в result"
            st.success("Все верно! Ключ = 79")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
