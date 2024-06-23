import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import numpy as np


hide_part_of_page()
st.subheader("HW9. Блок Numpy. Задача 2")
st.markdown(
    "- Создайте переменную **array_two** и присвойте ей значение сгенерированной матрицы случайными значениями при помощи numpy **размером 11 строк на 8 столбцов** (должен быть тип переменной numpy.ndarray)\n"
    "- Создайте переменную **array_three** и присвойте ей значение сгенерированной матрицы случайными значениями при помощи numpy **размером 11 строк на 1 столбец** (должен быть тип переменной numpy.ndarray)\n"
    "- Создайте переменную **result** и присвойте ей значение переменожения **транспонированной матрицы array_two** на матрицу **array_three**\n"
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
            # array_two
            assert "array_two" in loc.keys(), "Проверьте название переменной array_two"
            assert isinstance(
                loc["array_two"], np.ndarray
            ), "Проверьте тип переменной array_one"
            assert loc["array_two"].shape == (
                11,
                8,
            ), "Проверьте размер матрицы array_two"

            # array_three
            assert (
                "array_three" in loc.keys()
            ), "Проверьте название переменной array_three"
            assert isinstance(
                loc["array_three"], np.ndarray
            ), "Проверьте тип переменной array_three"
            assert loc["array_three"].shape == (
                11,
                1,
            ), "Проверьте размер матрицы array_three"

            # result
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert isinstance(
                loc["result"], np.ndarray
            ), "Проверьте тип переменной result"
            assert loc["result"].shape == (8, 1), "Проверьте размер матрицы result"
            # assert np.array_equal(
            #     loc["result"],
            #     np.dot(loc["array_two"].T, loc["array_three"]),
            #     equal_nan=True,
            # ), "Проверьте результат умножения матриц в result"
            assert np.allclose(
                loc["result"], np.dot(loc["array_two"].T, loc["array_three"])
            ), "Проверьте результат умножения матриц в result"
            st.success("Все верно! Ключ = 60")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
