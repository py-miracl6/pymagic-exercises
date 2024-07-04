import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import numpy as np


hide_part_of_page()
st.subheader("HW9. Блок Numpy. Задача 4")
st.markdown(
    "- Создайте переменную **array_four** и присвойте ей значение сгенерированной матрицы случайными значениями при помощи numpy **размером 11 строк на 8 столбцов** (должен быть тип переменной numpy.ndarray)\n"
    "- Получите сингулярное разложение матрицы **array_four** при помощи numpy, запишите в соответствующие переменные **U, S, Vt**, где:\n"
    "   - **U** - ортогональная матрица\n"
    "   - **S** - массив, числа которого используются в диагональной матрице $\Sigma$\n"
    "   - **Vt** - ортогональная матрица в уже транспонированном виде (ничего транспонировать самим не нужно)\n"
    "- Создайте переменную **result** и присвойте ей значение переменожения **U**, **S** и **Vt**, где от матрицы **u** необходимо взять по 8 строк и 8 столбцов (подсказка U[:8, :8]@ ....)"
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
            # array_four
            assert (
                "array_four" in loc.keys()
            ), "Проверьте название переменной array_four"
            assert isinstance(
                loc["array_four"], np.ndarray
            ), "Проверьте тип переменной array_one"
            assert loc["array_four"].shape == (
                11,
                8,
            ), "Проверьте размер матрицы array_four"

            # U
            assert "U" in loc.keys(), "Проверьте название переменной U"
            assert isinstance(loc["U"], np.ndarray), "Проверьте тип переменной U"

            # S
            assert "S" in loc.keys(), "Проверьте название переменной S"
            assert isinstance(loc["S"], np.ndarray), "Проверьте тип переменной S"

            # Vt
            assert "Vt" in loc.keys(), "Проверьте название переменной Vt"
            assert isinstance(loc["Vt"], np.ndarray), "Проверьте тип переменной Vt"

            # result
            assert "result" in loc.keys(), "Проверьте название переменной result"
            assert isinstance(
                loc["result"], np.ndarray
            ), "Проверьте тип переменной result"
            assert np.allclose(
                loc["result"], loc["U"][:8, :8] @ np.diag(loc["S"]) @ loc["Vt"]
            ), "Проверьте результат в переменной result"
            assert (
                "svd(" in content
            ), "Проверьте, что вы действительно сделали сингулярное разложение матрицы array_four"
            st.success("Все верно! Ключ = 17")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
