from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:
    return lambda ts: ts if ts < 2 else fibonacci(0, 1, 1, ts)


@tail_call_optimized
def fibonacci(prev_value, curr_value, curr_step, target_step):
    if curr_step == target_step:
        return curr_value
    return fibonacci(curr_value, prev_value+curr_value, curr_step+1, target_step)


if __name__ == '__main__':
    print(fibonacci_impl()(5))
