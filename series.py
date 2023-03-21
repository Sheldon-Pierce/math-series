def fibonacci(n):
    """
    The next number is found by adding up the two numbers before it:
        - the 2 is found by adding the two numbers before it (1+1),
        the 3 is found by adding the two numbers before it (1+2),
        the 5 is (2+3)
    :param n:
    1, 2, 4, 15
    :return:
    0, 1, 1, 2
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):
    """
    As with the Fibonacci numbers, each Lucas number is defined to be the sum of its two immediately previous terms
    :param n:
    Any number greater than 0
    :return:
    2, 1, 3, 4, 7, 11
    """

    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, y=0, z=1):
    """
    Depending on the input of the variables, you will get a different sequence.
    :param n:
    The nth number in the sequence
    :param y:
    Leave as is for Fibonacci, change to 2 for Lucas
    :param z:
    Leave as is for Fibonacci, change to 1 for Lucas
    :return:
    """

    if y == 0 and z == 1:
        return fibonacci(n)
    if y == 2 and z == 1:
        return lucas(n)
    else:
        if n == 0:
            return y
        if n == 1:
            return z
        return sum_series(n-1, y, z) + sum_series(n-2, y, z)


