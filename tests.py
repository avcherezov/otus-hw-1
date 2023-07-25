import math


def solve(a, b, c):
    root = []
    epsilon = math.ulp(1.0)

    if (
        not isinstance(a, float | int)
        or not isinstance(b, float | int)
        or not isinstance(c, float | int)
    ):
        return Exception('только числа')

    if a <= epsilon:
        return Exception('ноль нельзя')

    discr = b ** 2 - 4 * a * c

    if discr < -epsilon:
        return root
    elif discr > epsilon:
        root.append('x1')
        root.append('x2')
        return root
    elif discr <= epsilon:
        root.append('x1')
        return root


def test_1():
    response = solve(a=1, b=0, c=1)
    assert len(response) == 0


def test_2():
    response = solve(a=1, b=0, c=-1)
    assert len(response) == 2


def test_3():
    response = solve(a=1e-15, b=1e-15, c=1e-15)
    assert len(response) == 1


def test_4():
    response = solve(a=0, b=0, c=0)
    assert isinstance(response, Exception)
    assert response.args[0] == 'ноль нельзя'


def test_5():
    response = solve(a='x1', b='x2', c='x3')
    assert isinstance(response, Exception)
    assert response.args[0] == 'только числа'
