import pytest
import bonus_calculator


@pytest.mark.parametrize(
    "salary, mark, grade, expected_error, expected_result",
    [
        (60000, 1, 7, ValueError, 0),
        (100000, 2, 7, None, 26250.0),
        (150000, 2.5, 7, None, 78750.0),
        (400000, 3, 7, None, 420000.0),
        (750000, 3.5, 7, None, 1181250.0),
        (750000, 5, 11, None, 1650000.0),
        (400000, 6, 11, ValueError, 0),
        (150000, 6, 14, ValueError, 0),
        (100000, 5, 14, None, 230000.0),
        (60000, 3.5, 14, ValueError, 0),
        (60000, 3, 11, ValueError, 0),
        (100000, 2.5, 11, None, 55000.0),
        (150000, 1, 11, None, 0),
        (400000, 2, 14, None, 115000.0),
        (750000, 2, 17, None, 225000.0),
        (750000, 1, 14, None, 0),
        (400000, 2.5, 17, None, 240000.0),
        (150000, 3.5, 17, None, 270000.0),
        (100000, 3, 17, None, 120000.0),
        (60000, 6, 17, ValueError, 0),
        (60000, 5, 19, ValueError, 0),
        (100000, 6, 19, ValueError, 0),
        (150000, 5, 7, None, 315000.0),
        (400000, 3.5, 19, ValueError, 0),
        (750000, 3, 19, ValueError, 0),
        (150000, 2, 19, ValueError, 0),
        (750000, 2.5, 19, ValueError, 0),
        (400000, 1, 19, ValueError, 0),
        (100000, 1, 17, None, 0),
        (60000, 2.5, 14, ValueError, 0),
        (60000, 2, 11, ValueError, 0),
        (100000, 3.5, 11, None, 165000.0),
        (400000, 5, 17, None, 960000.0),
        (750000, 6, 7, ValueError, 0),
        (150000, 3, 14, None, 172500.0),
    ],
)
def test_calculate_salary_bonus(salary, mark, grade, expected_error, expected_result):
    check_calc_bonus_pairwise(salary, mark, grade, expected_error, expected_result),


def check_calc_bonus_pairwise(salary: int,
                              mark: float,
                              grade: int,
                              expected_error,
                              expected_result: float):
    res = 0
    if expected_error is not None:
        with pytest.raises(expected_error):
            res = bonus_calculator.calc_bonus(salary, mark, grade),
    else:
        res = bonus_calculator.calc_bonus(salary, mark, grade)
    assert res == expected_result
