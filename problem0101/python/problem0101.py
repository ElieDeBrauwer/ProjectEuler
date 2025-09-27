from functools import partial

import sympy


def evaluate_polynomial(poly: list[int], x: int) -> int:
    """
    Evaluate a polynomial using Horner's method.

    Args:
        poly: List of coefficients in descending order of degree
        x: Value at which to evaluate the polynomial

    Returns:
        Result of polynomial evaluation at x
    """
    res = poly[0]
    for i in poly[1:]:
        res = res * x + i
    return res


def test_un():
    """
    Returns:
        The test function (n**3)
    """
    polynomial_test = [1, 0, 0, 0]  # n_3
    return partial(evaluate_polynomial, polynomial_test)


def real_un():
    """
    Returns:
        The real target function.
    """
    polynomial_final = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
    return partial(evaluate_polynomial, polynomial_final)


def run_0101(un) -> None:
    """
    Solution is based around sympy.interpolate. By feeding it a
    growing sequence of term it returns the correct interpolating function (OP).
    """
    n = sympy.symbols("n")
    k = 1
    fit_sum = 0

    while True:
        # Construct the OP()
        terms = [(i, un(i)) for i in range(1, k + 1)]
        print(f"k={k} - terms={terms}")
        op = sympy.interpolate(terms, n)
        print(f"OP of degree {k}: {op}")

        # Verify the first k-1 values are equal
        for values in range(1, k):
            assert un(values) == op.subs(n, values)

        # Calculate fit
        target_value = un(k + 1)
        fit_value = op.subs(n, k + 1)
        print(f"FIT value {fit_value} - target {target_value}")

        # Stop condition.
        if target_value == fit_value:
            print("Target polynomial found, stopping")
            break
        else:
            fit_sum += fit_value

        k = k + 1

    print(f"Sum of FITs: {fit_sum}")


if __name__ == "__main__":
    run_0101(test_un())
    run_0101(real_un())
