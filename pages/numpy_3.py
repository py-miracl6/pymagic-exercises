import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import numpy as np


hide_part_of_page()
st.subheader("HW9. Блок Numpy. Задача 3")
st.markdown(
    "- Создайте переменную **array_one** и присвойте ей значение сгенерированной матрицы случайными значениями при помощи numpy **размером 6 строк на 11 столбцов** (должен быть тип переменной numpy.ndarray)\n"
    "- Создайте переменную **array_two** и присвойте ей значение сгенерированной матрицы случайными значениями при помощи numpy **размером 11 строк на 8 столбцов** (должен быть тип переменной numpy.ndarray)\n"
    "- Создайте переменную **array_one_t** и присвойте ей матрицу **array_one** с измененным размером, где она будет иметь 33 строки и 2 столбца (то есть, по итогу мы должны в array_one_t получить матрицу из array_one размером (33,2))\n"
    "- Создайте переменную **rang_1** и присвойте ей значение найденного ранга матрицы **array_one_t** при помощи numpy\n"
    "- Создайте переменную **rang_2** и присвойте ей значение найденного ранга матрицы **array_two** при помощи numpy"
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

            # array_two
            assert "array_two" in loc.keys(), "Проверьте название переменной array_two"
            assert isinstance(
                loc["array_two"], np.ndarray
            ), "Проверьте тип переменной array_two"
            assert loc["array_two"].shape == (
                11,
                8,
            ), "Проверьте размер матрицы array_two"

            # array_one_t
            assert (
                "array_one_t" in loc.keys()
            ), "Проверьте название переменной array_one_t"
            assert isinstance(
                loc["array_one_t"], np.ndarray
            ), "Проверьте тип переменной array_one_t"
            assert loc["array_one_t"].shape == (
                33,
                2,
            ), "Проверьте размер матрицы array_one_t"
            assert np.array_equal(
                loc["array_one_t"], loc["array_one"].reshape(33, 2), equal_nan=True
            ), "Проверьте значения в матрице array_one_t"

            # rang_1
            assert "rang_1" in loc.keys(), "Проверьте название переменной rang_1"
            assert isinstance(
                loc["rang_1"], (np.int64, np.int32)
            ), "Проверьте тип переменной rang_1"
            assert loc["rang_1"] == np.linalg.matrix_rank(
                loc["array_one_t"]
            ), "Проверьте результат в переменной rang_1"
            assert (
                "matrix_rank(array_one_t" in content
            ), "Проверьте, что вы действительно ищите ранг матрицы при помощи numpy (linalg)"

            # rang_2
            assert "rang_2" in loc.keys(), "Проверьте название переменной rang_2"
            assert isinstance(
                loc["rang_2"], (np.int64, np.int32)
            ), "Проверьте тип переменной rang_2"
            assert loc["rang_2"] == np.linalg.matrix_rank(
                loc["array_two"]
            ), "Проверьте результат в переменной rang_2"
            assert (
                "matrix_rank(array_two" in content
            ), "Проверьте, что вы действительно ищите ранг матрицы при помощи numpy (linalg)"

            st.success("Все верно! Ключ = 88")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
