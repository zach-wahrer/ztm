from random_game import guess_result, guess_validation
import unittest


class TestRandomGame(unittest.TestCase):

    def test_guess_result_valid(self):
        self.assertTrue(guess_result(1, 1))

    def test_guess_result_invalid(self):
        self.assertFalse(guess_result(None, 8))

    def test_guess_result_no_match(self):
        self.assertFalse(guess_result(1, 8))

    def test_guess_validation_valid(self):
        input = guess_validation(5, 1, 10)
        output = 5
        self.assertEqual(input, output)

    def test_guess_validation_non_number(self):
        input = guess_validation('abc', 1, 10)
        output = None
        self.assertEqual(input, output)

    def test_guess_validation_outside_range_lesser(self):
        input = guess_validation(1, 2, 10)
        output = None
        self.assertEqual(input, output)

    def test_guess_validation_outside_range_greater(self):
        input = guess_validation(11, 2, 10)
        output = None
        self.assertEqual(input, output)
