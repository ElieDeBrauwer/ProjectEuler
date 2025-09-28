import time


def num_divisors(n: int) -> int:
    """
    Calculates the number of divisors are given value has.

    Params:
        n (int): Original number

    Return:
        (int): Number of divisors
    """
    count = 0
    candidate = 1
    while candidate * candidate < n:
        if n % candidate == 0:
            count = count + 2
        candidate = candidate + 1

    if candidate * candidate == n:
        count = count + 1

    return count


if __name__ == "__main__":
    start = time.time_ns()
    n = 0
    max_val = 0
    i = 0
    while True:
        num_div = num_divisors(n * n)
        num_solutions = (num_div + 1) / 2
        if num_solutions > max_val:
            print(
                f"n={n} -> n^2={n * n} -> number of divisors = {num_div} -> number of solutions = {num_solutions}"
            )
            max_val = num_solutions
            if num_solutions >= 1000:
                break

        i = i + 1
        if i == 1000:
            i = 0
            print(
                f"n={n} -> current max = {max_val}"
            )

        n = n + 1

    end = time.time_ns()
    print(f"Duration {(end - start) / 1e9}s")
