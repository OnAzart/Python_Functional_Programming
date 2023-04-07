from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def factorial_impl() -> Callable[[int], int]:
    return lambda n: factorial(n)


if __name__ == '__main__':
    print(factorial_impl()(6))
