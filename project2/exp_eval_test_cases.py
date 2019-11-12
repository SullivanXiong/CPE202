import unittest
from exp_eval import infix_to_postfix
from exp_eval import postfix_eval
from exp_eval import operate
from exp_eval import postfix_valid

class TestCase(unittest.TestCase):

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("7 + 2 * ( ( 9 - 2 ) * 3 )"), "7 2 9 2 - 3 * * +")
        self.assertEqual(infix_to_postfix("( 7 ^ 2 * 7 ) ^ ( 1 / 3 )"), "7 2 ^ 7 * 1 3 / ^")
        self.assertEqual(infix_to_postfix("( ~ 2 ) ^ 2"), "2 ~ 2 ^")

    def test_postfix_eval(self):
        self.assertEqual(postfix_eval("7 2 9 2 - 3 * * +"), 49)
        self.assertAlmostEqual(postfix_eval("7 2 ^ 7 * 1 3 / ^"), 7, 11)
        self.assertEqual(postfix_eval("2 ~ 2 ^"), 4)
        self.assertRaises(ZeroDivisionError, postfix_eval, "5 0 /")
        self.assertRaises(SyntaxError, postfix_eval, "5 +")
        self.assertRaises(SyntaxError, postfix_eval, "5 2 7 +")
        self.assertRaises(SyntaxError, postfix_eval, "5 b +")

    def test_operate(self):
        self.assertEqual(operate("2", "6", "+"), 8)
        self.assertEqual(operate("2", "6", "-"), 4)
        self.assertEqual(operate("2", "6", "*"), 12)
        self.assertEqual(operate("2", "6", "/"), 3)
        self.assertEqual(operate("2", "6", "^"), 36)
        self.assertRaises(ZeroDivisionError, operate, "0", "6", "/")

    def test_postfix_valid(self):
        self.assertEqual(postfix_valid("7 2 ^ 7 * 1 3 / ^"), True)
        self.assertEqual(postfix_valid("7 2 ^ 7 * 1 3 / "), False)
        self.assertEqual(postfix_valid("3 7 2 ^ 7 * 1 3 / ^"), False)


def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()