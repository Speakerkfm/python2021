import pytest
import bonus_calculator

test_cases = {
    0: [60000, -1, 5, ValueError, 0],
    1: [100000, 1, 5, ValueError, 0],
    2: [750001, 2, 5, ValueError, 0],
    3: [750001, 2.5, 7, ValueError, 0],
    4: [100000, 3, 7, None, 105000.00],
    5: [60000, 3.5, 7, ValueError, 0],
    6: [60000, 5, 11, ValueError, 0],
    7: [100000, 6, 11, ValueError, 0],
    8: [750001, 6, 14, ValueError, 0],
    9: [750001, 5, 17, ValueError, 0],
    10: [100000, 3.5, 17, None, 165000.00],
    11: [60000, 2.5, 17, ValueError, 0],
    12: [60000, 2, 14, ValueError, 0],
    13: [100000, -1, 14, ValueError, 0],
    14: [750001, 3, 11, ValueError, 0],
    15: [750001, 1, 19, ValueError, 0],
    16: [100000, 2, 19, ValueError, 0],
    17: [60000, 1, 11, ValueError, 0],
    18: [60000, 3, 19, ValueError, 0],
    19: [100000, 2.5, 11, None, 55000.00],
    20: [750001, -1, 11, ValueError, 0],
    21: [750001, 3.5, 11, ValueError, 0],
    22: [100000, 5, 19, ValueError, 0],
    23: [60000, 6, 19, ValueError, 0],
    24: [60000, 6, 5, ValueError, 0],
    25: [60000, 5, 5, ValueError, 0],
    26: [60000, 3.5, 5, ValueError, 0],
    27: [60000, -1, 19, ValueError, 0],
    28: [60000, 2.5, 19, ValueError, 0],
    29: [60000, 3, 5, ValueError, 0],
    30: [60000, 1, 14, ValueError, 0],
    31: [60000, 2, 11, ValueError, 0],
    32: [60000, 2, 17, ValueError, 0],
    33: [60000, 1, 17, ValueError, 0],
    34: [60000, 3, 17, ValueError, 0],
    35: [60000, 2.5, 5, ValueError, 0],
    36: [60000, -1, 17, ValueError, 0],
    37: [60000, 3.5, 19, ValueError, 0],
    38: [60000, 5, 14, ValueError, 0],
    39: [60000, 6, 17, ValueError, 0],
    40: [60000, 6, 7, ValueError, 0],
    41: [60000, 5, 7, ValueError, 0],
    42: [60000, 3.5, 14, ValueError, 0],
    43: [60000, -1, 7, ValueError, 0],
    44: [60000, 2.5, 14, ValueError, 0],
    45: [60000, 3, 14, ValueError, 0],
    46: [60000, 1, 7, ValueError, 0],
    47: [60000, 2, 7, ValueError, 0],
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
