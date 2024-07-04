import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import numpy as np


hide_part_of_page()
st.subheader("HW9. Блок Numpy. Задача 5")
st.markdown(
    "- Вам дана матрица **X_matrix** ниже (скопируйте код и вставьте в code editor)\n"
    "- Необходимо вычислить собственные векторы и собственные значения матрицы **X_matrix** при помощи numpy:\n"
    "   - Создайте переменную **w** и присвойте ей массив с собственными значениями матрицы X_matrix (тип numpy.ndarray)\n"
    "   - Создайте переменную **v** и присвойте ей матрицу с собственными векторами матрицы X_matrix (тип numpy.ndarray)\n"
    "- Проверьте, что при умножении матрицы X_matrix и собственного вектора, получается тот же результат, что и при умножении собственного значения и собственного вектора, для этого:\n"
    "   - Создайте переменную **check_1** и присвойте ей результат перемножения матрицы X_matrix на собственный вектор из **v** с нулевым индексом\n"
    "   - Создайте переменную **check_2** и присвойте ей результат перемножения собственного вектора **v** с нулевым индексом на собственное значение **w** с нулевым индексом\n"
    "\n**Подсказка:**\n"
    "Получившийся результат в **check_1** должен быть равен **check_2**"
)
st.code("X_matrix = np.array([[-1, -6], [2, 6]])", language="python")

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
X_matrix_check = np.array([[-1, -6], [2, 6]])
w_check, v_check = np.linalg.eig(X_matrix_check)
check_1_check = np.dot(X_matrix_check, v_check[:, 0])
check_2_check = np.dot(v_check[:, 0], w_check[0])

if content:
    st.markdown("### Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        try:
            # X_matrix
            assert "X_matrix" in loc.keys(), "Проверьте название переменной X_matrix"
            assert isinstance(
                loc["X_matrix"], np.ndarray
            ), "Проверьте тип переменной array_one"
            assert loc["X_matrix"].shape == (
                2,
                2,
            ), "Проверьте размер матрицы X_matrix"
            assert np.array_equal(
                loc["X_matrix"], X_matrix_check
            ), "Проверьте результат в переменной X_matrix"

            # w
            assert "w" in loc.keys(), "Проверьте название переменной w"
            assert isinstance(loc["w"], np.ndarray), "Проверьте тип переменной w"
            assert np.allclose(loc["w"], w_check), "Проверьте результат в переменной w"

            # v
            assert "v" in loc.keys(), "Проверьте название переменной v"
            assert isinstance(loc["v"], np.ndarray), "Проверьте тип переменной v"
            assert np.allclose(loc["v"], v_check), "Проверьте результат в переменной v"

            # check_1
            assert "check_1" in loc.keys(), "Проверьте название переменной check_1"
            assert isinstance(
                loc["check_1"], np.ndarray
            ), "Проверьте тип переменной check_1"

            # check_2
            assert "check_2" in loc.keys(), "Проверьте название переменной check_2"
            assert isinstance(
                loc["check_2"], np.ndarray
            ), "Проверьте тип переменной check_2"

            # check result 1
            assert np.allclose(
                loc["check_1"], check_1_check
            ), "Проверьте, верно ли вы умножили X_matrix на нулевой вектор (проблема в индексах)"
            assert np.allclose(
                loc["check_2"], check_1_check
            ), "Проверьте, верно ли вы умножили нулевой вектор на собственное значение под 0-ым индексом (проблема в индексах)"
            st.success("Все верно! Ключ = 71")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
