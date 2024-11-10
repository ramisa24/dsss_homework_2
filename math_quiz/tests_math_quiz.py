import unittest
from math_quiz import generate_random_number, find_random_operator, create_problem_and_solution


class TestMathQuiz(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # Test multiple random values
            random_value = generate_random_number(min_value, max_value)
            self.assertTrue(min_value <= random_value <= max_value)

    def test_find_random_operator(self):
        # Test if the operator selected is one of the expected values '+', '-', '%', '*'
        valid_operators = ['+', '-', '%', '*']
        for _ in range(1000):
            operator = find_random_operator()
            self.assertIn(operator, valid_operators)

    def test_create_problem_and_solution(self):
        # Define test cases for different operators
        test_cases = [
            (3, 2, '+', '3 + 2', 5),
            (5, 3, '-', '5 - 3', 2),
            (3, 6, '*', '3 * 6', 18),
            (4, 2, '%', '4 % 2', 0)
        ]

        for value_1, value_2, operator, desired_problem, desired_answer in test_cases:
            problem, answer = create_problem_and_solution(value_1, value_2, operator)
            self.assertEqual(problem, desired_problem)
            self.assertEqual(answer, desired_answer)


if __name__ == "__main__":
    unittest.main()

