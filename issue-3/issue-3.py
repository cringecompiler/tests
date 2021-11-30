from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestFT(unittest.TestCase):
    def test_eq(self):
        actual = fit_transform(['hello', 'there', 'general', 'Kenobi'])
        expected = [('hello', [0, 0, 0, 1]),
                    ('there', [0, 0, 1, 0]),
                    ('general', [0, 1, 0, 0]),
                    ('Kenobi', [1, 0, 0, 0])]

        self.assertEqual(actual, expected)

    def test_in(self):
        actual = fit_transform(['ios', 'web', 'ios', 'android'])
        expected = [[('a', [0, 0, 1]),
                     ('b', [0, 1, 0]),
                     ('c', [1, 0, 0])], [('hello', [0, 0, 0, 1]),
                                         ('there', [0, 0, 1, 0]),
                                         ('general', [0, 1, 0, 0]),
                                         ('Kenobi', [1, 0, 0, 0])]]

        self.assertNotIn(actual, expected)

    def test_a(self):
        actual = fit_transform(['green', 'blue', 'blue', 'green'])

        self.assertIsInstance(actual, list)

    def test_ex(self):
        with self.assertRaises(Exception):
            fit_transform()


if __name__ == '__main__':
    from pprint import pprint

    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities
    unittest.main()
