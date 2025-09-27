import unittest

from problem0101.python.problem0101 import evaluate_polynomial, test_un


class TestProblem0101(unittest.TestCase):
    def test_evaluation_polynomial(self):
        polynomial = [-9, 5, 1]
        x = 1
        assert evaluate_polynomial(polynomial, x) == (-9 * x**2 + 5 * x + 1)

        polynomial = [1, 0, 0, 0]
        for x in range(10):
            assert evaluate_polynomial(polynomial, x) == x**3

    def test_un(self):
        un = test_un()
        assert un(3) == 3**3

        polynomial = [1, 0, 0, 0]
        for x in range(10):
            assert evaluate_polynomial(polynomial, x) == x**3


if __name__ == "__main__":
    unittest.main()
