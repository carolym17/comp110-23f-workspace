"""Print versus return gradescope"""

def f(x: int) -> int:
    print(x)
    x *= 2
    return x

y: int = f(3)


def f(x: int) -> int:
    return x
    x *= 2
    print(x)

y: int = f(3)