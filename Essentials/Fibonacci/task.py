from typing import Callable


def fibonacci(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    return fibonacci(value-1) + fibonacci(value-2)
    # raise Exception("Implement me")


def fibonacci_impl() -> Callable[[int], int]:
    return lambda v: fibonacci(v)


if __name__ == '__main__':
    print(fibonacci_impl()(4))
