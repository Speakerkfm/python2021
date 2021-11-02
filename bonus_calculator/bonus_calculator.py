from allpairspy import AllPairs


def calc_bonus(salary: int, mark: float, grade: int) -> int:
    if 70000 > salary or salary > 750000:
        raise ValueError('salary must be [70000...750000]')
    if 1 > mark or mark > 5:
        raise ValueError('mark must be [1...5]')
    if 7 > grade or grade > 17:
        raise ValueError('grade mus be [7...17]')

    bonus = 0
    if grade < 10:
        bonus = 1.05 * salary
    if 10 <= grade < 13:
        bonus = 1.1 * salary
    if 13 <= grade < 15:
        bonus = 1.15 * salary
    if 15 <= grade:
        bonus = 1.1 * salary

    bonus_modifier = 0
    if mark < 2:
        bonus_modifier = 0
    if 2 <= mark < 2.5:
        bonus_modifier = 0.25
    if 2.5 <= mark < 3:
        bonus_modifier = 0.5
    if 3 <= mark < 3.5:
        bonus_modifier = 1
    if 3.5 <= mark < 4:
        bonus_modifier = 1.5
    if 4 <= mark:
        bonus_modifier = 2

    return round(bonus * bonus_modifier, 2)


if __name__ == '__main__':
    parameters = [
        [60000, 100000, 750001],
        [-1, 1, 2, 2.5, 3, 3.5, 5, 6],
        [5, 7, 11, 14, 17, 19],
    ]

    print("PAIRWISE:")
    for i, pairs in enumerate(AllPairs(parameters)):
        print("{:2d}: {}".format(i, pairs))
