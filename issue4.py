from typing import List, Tuple
import pytest


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


def test_ft_eq_1():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)

    assert transformed_cities == exp_transformed_cities


def test_ft_notin():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    transformed_cities = fit_transform(cities)
    member = ['Moscow', [0, 1, 0]]

    assert member not in transformed_cities


def test_ft_eq_2():
    countries = ['Russia', 'USA', 'Russia', 'UK', 'Ukraine', 'UK']
    exp_transformed_countries = [
        ('Russia', [0, 0, 0, 1]),
        ('USA', [0, 0, 1, 0]),
        ('Russia', [0, 0, 0, 1]),
        ('UK', [0, 1, 0, 0]),
        ('Ukraine', [1, 0, 0, 0]),
        ('UK', [0, 1, 0, 0]),
    ]
    transformed_countries = fit_transform(countries)

    assert transformed_countries == exp_transformed_countries


def test_ft_not_eq():
    cities = ['Moscow', 'New York', 'London', 'Moscow']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)

    assert transformed_cities != exp_transformed_cities


def test_exception():
    with pytest.raises(TypeError):
        fit_transform()


if __name__ == '__main__':
    pytest.main()
