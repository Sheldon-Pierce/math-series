import pytest
from series import fibonacci
from series import lucas
from series import sum_series


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_20():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_lucas1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas5():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas10():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_sum_series():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_sum_series():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected

def test_sum_series():
    actual = sum_series(5, 3, 3)
    expected = 24
    assert actual == expected
