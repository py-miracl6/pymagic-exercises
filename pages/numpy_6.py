import streamlit as st
from streamlit_ace import st_ace
from utils.help_func import stdoutIO, hide_part_of_page
import numpy as np
from scipy import spatial


hide_part_of_page()
st.subheader("HW9. Блок Numpy. Задача 6")
st.markdown(
    "- Вам даны два вектора **a** и **b** ниже (скопируйте код и вставьте в code editor)\n"
    "- Создайте переменную **similarity** и присвойте значение косинуса угла между векторами **a** и **b** (можно использовать scipy)\n"
    "- Найдите длины векторов:\n"
    "   - Создайте переменную **dist_a_manh** и присвойте значение Манхэттенской нормы вектора **a**\n"
    "   - Создайте переменную **dist_b_manh** и присвойте значение Манхэттенской нормы вектора **b**\n"
    "   - Создайте переменную **dist_a_euclid** и присвойте значение Евклидовой нормы вектора **a**\n"
    "   - Создайте переменную **dist_b_euclid** и присвойте значение Евклидовой нормы вектора **b**"
)
st.code("a = np.array([2, 4, 5])\n" "b = np.array([1, 3, 2])", language="python")

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

a_check = np.array([2, 4, 5])
b_check = np.array([1, 3, 2])

dict_check = {
    "similarity": 1 - spatial.distance.cosine(a_check, b_check),
    "dist_a_manh": np.linalg.norm(a_check, ord=1),
    "dist_b_manh": np.linalg.norm(b_check, ord=1),
    "dist_a_euclid": np.linalg.norm(a_check, ord=2),
    "dist_b_euclid": np.linalg.norm(b_check, ord=2),
}


def testing(data, key, dict_data):
    assert key in data.keys(), f"Проверьте название переменной {key}"
    assert isinstance(data[key], (float, int)), f"Проверьте тип переменной {key}"
    assert round(data[key], 4) == round(
        dict_data[key], 4
    ), f"Проверьте результат в переменной {key}"


if content:
    st.markdown("### Результат")
    try:
        with stdoutIO() as s:
            exec(content, globals(), loc)
        st.write(s.getvalue())
        try:
            # a
            assert "a" in loc.keys(), "Проверьте название переменной a"
            assert isinstance(loc["a"], np.ndarray), "Проверьте тип переменной a"
            assert np.array_equal(
                loc["a"], a_check
            ), "Проверьте результат в переменной a"

            # b
            assert "b" in loc.keys(), "Проверьте название переменной b"
            assert isinstance(loc["b"], np.ndarray), "Проверьте тип переменной b"
            assert np.array_equal(
                loc["b"], b_check
            ), "Проверьте результат в переменной b"

            for k in dict_check.keys():
                testing(data=loc, key=k, dict_data=dict_check)

            # check result 1
            # assert np.allclose(
            #     loc["check_1"], check_1_check
            # ), "Проверьте, верно ли вы умножили X_matrix на нулевой вектор (проблема в индексах)"
            # assert np.allclose(
            #     loc["check_2"], check_1_check
            # ), "Проверьте, верно ли вы умножили нулевой вектор на собственное значение под 0-ым индексом (проблема в индексах)"
            st.success("Все верно! Ключ = 19")
        except Exception as ex:
            st.error(ex)
    except Exception as ex:
        st.error(ex)
