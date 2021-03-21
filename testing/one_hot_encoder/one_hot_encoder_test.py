import unittest
import one_hot_encoder


class TestEncoder(unittest.TestCase):
    def test_ok_four_cities_with_copies(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)
        self.assertNotIn(('Moscow', [1, 0, 0]), actual)

    def test_ok_two_diff_cities(self):
        cities = ['Moscow', 'Perm']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 1]),
            ('Perm', [1, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_ok_two_same_cities(self):
        cities = ['Moscow', 'Moscow']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [1]),
            ('Moscow', [1]),
        ]
        self.assertEqual(actual, expected)

    def test_empty_args(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform()
