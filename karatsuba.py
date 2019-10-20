""" Karatsuba algorithm

    Single digit multpilication recursive algorithm 
"""


def multiply(x, y):
    """ multiply two numbers """
    str_x = str(x)
    str_y = str(y)
    n = max([len(str_x), len(str_y)])
    if n == 1:
        return x * y
    if n % 2:
        n += 1
    str_x = str_x.zfill(n)
    str_y = str_y.zfill(n)
    half = n // 2
    a = int(str_x[:half])
    b = int(str_x[half:])
    c = int(str_y[:half])
    d = int(str_y[half:])
    ac = multiply(a, c)
    bd = multiply(b, d)
    adbc = multiply(a + b, c + d) - ac - bd  # gauss "trick"
    return 10 ** n * ac + 10 ** (n / 2) * (adbc) + bd


if __name__ == '__main__':
    assert multiply(12, 13) == 156
    assert multiply(123, 13) == 1599
    assert multiply(1234, 5678) == 7006652
    assert multiply(12345, 67891) == 838114395

