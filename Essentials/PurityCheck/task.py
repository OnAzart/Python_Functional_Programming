from typing import Callable

global test
test = 1


class Integer:
    def __init__(self, value: int):
        self.value = value


def increment(obj1: Integer):
    global test
    test = 2
    return Integer(obj1.value + 1)


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    def not_affecting_globals():
        prev_globals = globals().copy()
        increment_fn(Integer(1))
        if prev_globals == globals().copy():
            return True

    def check_for_no_mutability():
        int1 = Integer(1)
        int2 = increment_fn(int1)
        return False if int1 == int2 else True

    # suit to pass check from result
    def check_changes_handling():
        int1 = Integer(1)
        int2 = increment_fn(int1)
        int12 = increment_fn(int1)

        fst_condition = (int1.value + 1) == int2.value and (int1.value + 1) == int12.value

        int1 = Integer(1)
        int2 = increment_fn(int1)
        int3 = increment_fn(int2)
        sec_condition = (int1.value + 1) == int2.value and (int2.value + 1) == int3.value
        return fst_condition and sec_condition

    if not_affecting_globals() and check_for_no_mutability() and check_for_no_mutability():
        return True
    return False


if __name__ == '__main__':
    print(is_pure(increment))
    input = Integer(1)
    res1 = increment(input)
    res2 = increment(input)
