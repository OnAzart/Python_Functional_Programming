import random
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from math import sqrt, ceil  # optimize and evaluate
from functools import wraps
from time import process_time


numbers = [random.randint(0, 500000) for n in range(100000)]


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(process_time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(process_time() * 1000)) - start
            print(
                f"Total execution time {func.__name__}: {end_ if end_ > 0 else 0} ms"
            )

    return _time_it


# @measure
def is_prime_imperative(n: int) -> bool:
    for possible_divider in range(2, int(sqrt(n)+1)):
        if (n / possible_divider).is_integer():
            return False
    return True


# @measure
def is_prime(n: int) -> bool:
    def is_prime_recursive(border, number_to_check, curr_number):
        if (number_to_check / curr_number).is_integer():
            return False
        if curr_number == border:
            return True
        return is_prime_recursive(border, number_to_check, curr_number + 1)

    if n in range(1, 4):
        return True
    return is_prime_recursive(int(sqrt(n)+1), n, 2)


@measure
def parallel_prime(prime_func):
    res = []
    with ThreadPoolExecutor() as executor:
        for bool_is_prime in executor.map(prime_func, numbers):
            res.append(bool_is_prime)
    print(res.count(True))


if __name__ == '__main__':
    parallel_prime(prime_func=is_prime_imperative)
    parallel_prime(prime_func=is_prime)

    # print(is_prime_imperative(507961))
    # print(is_prime(507961))
