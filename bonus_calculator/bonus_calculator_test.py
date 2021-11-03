import pytest
import bonus_calculator

test_cases = {
    0: [60000, 1, 7, ValueError, 0],
    1: [100000, 2, 7, None, 26250.0],
    2: [150000, 2.5, 7, None, 78750.0],
    3: [400000, 3, 7, None, 420000.0],
    4: [750000, 3.5, 7, None, 1181250.0],
    5: [750000, 5, 11, None, 1650000.0],
    6: [400000, 6, 11, ValueError, 0],
    7: [150000, 6, 14, ValueError, 0],
    8: [100000, 5, 14, None, 230000.0],
    9: [60000, 3.5, 14, ValueError, 0],
    10: [60000, 3, 11, ValueError, 0],
    11: [100000, 2.5, 11, None, 55000.0],
    12: [150000, 1, 11, None, 0],
    13: [400000, 2, 14, None, 115000.0],
    14: [750000, 2, 17, None, 225000.0],
    15: [750000, 1, 14, None, 0],
    16: [400000, 2.5, 17, None, 240000.0],
    17: [150000, 3.5, 17, None, 270000.0],
    18: [100000, 3, 17, None, 120000.0],
    19: [60000, 6, 17, ValueError, 0],
    20: [60000, 5, 19, ValueError, 0],
    21: [100000, 6, 19, ValueError, 0],
    22: [150000, 5, 7, None, 315000.0],
    23: [400000, 3.5, 19, ValueError, 0],
    24: [750000, 3, 19, ValueError, 0],
    25: [150000, 2, 19, ValueError, 0],
    26: [750000, 2.5, 19, ValueError, 0],
    27: [400000, 1, 19, ValueError, 0],
    28: [100000, 1, 17, None, 0],
    29: [60000, 2.5, 14, ValueError, 0],
    30: [60000, 2, 11, ValueError, 0],
    31: [100000, 3.5, 11, None, 165000.0],
    32: [400000, 5, 17, None, 960000.0],
    33: [750000, 6, 7, ValueError, 0],
    34: [150000, 3, 14, None, 172500.0],
}


def check_calc_bonus_pairwise(salary: int,
                              mark: float,
                              grade: int,
                              expected_exception,
                              expected_result: float,
                              test_name):
    res = 0
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            res = bonus_calculator.calc_bonus(salary, mark, grade)
    else:
        res = bonus_calculator.calc_bonus(salary, mark, grade)
    assert res == expected_result, test_name


def test_calc_bonus():
    for test_name, case in test_cases.items():
        check_calc_bonus_pairwise(case[0], case[1], case[2], case[3], case[4], test_name)
