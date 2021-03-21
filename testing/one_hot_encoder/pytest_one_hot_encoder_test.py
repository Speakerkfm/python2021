import pytest
import one_hot_encoder


def test_ok_four_cities_with_copies():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_ok_two_diff_cities():
    cities = ['Moscow', 'Perm']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 1]),
        ('Perm', [1, 0]),
    ]
    assert actual == expected


def test_ok_two_same_cities():
    cities = ['Moscow', 'Moscow']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [1]),
        ('Moscow', [1]),
    ]
    assert actual == expected


def test_empty_args():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()
