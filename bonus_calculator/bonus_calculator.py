from allpairspy import AllPairs


def validate_salary(salary: int):
    if 70000 > salary or salary > 750000:
        raise ValueError('salary must be [70000...750000]')


def validate_mark(mark: float):
    if 1 > mark or mark > 5:
        raise ValueError('mark must be [1...5]')


def validate_grade(grade: int):
    if 7 > grade or grade > 17:
        raise ValueError('grade must be [7...17]')


def calc_grade_bonus(grade: int) -> float:
    validate_grade(grade)

    if grade < 10:
        return 1.05
    if 10 <= grade < 13:
        return 1.1
    if 13 <= grade < 15:
        return 1.15
    if 15 <= grade:
        return 1.2


def calc_bonus_modifier(mark: float) -> float:
    validate_mark(mark)

    if mark < 2:
        return 0
    if 2 <= mark < 2.5:
        return 0.25
    if 2.5 <= mark < 3:
        return 0.5
    if 3 <= mark < 3.5:
        return 1
    if 3.5 <= mark < 4:
        return 1.5
    if 4 <= mark:
        return 2


def calc_bonus(salary: int, mark: float, grade: int) -> float:
    validate_salary(salary)
    result = calc_bonus_modifier(mark) * calc_grade_bonus(grade) * salary
    return round(result, 2)


if __name__ == '__main__':
    parameters = [
        [60000, 100000, 150000, 400000, 750000],
        [1, 2, 2.5, 3, 3.5, 5, 6],
        [7, 11, 14, 17, 19],
    ]

    print("PAIRWISE:")
    for i, pairs in enumerate(AllPairs(parameters)):
        print("{}".format(tuple(pairs)))
