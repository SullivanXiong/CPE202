'''Contains test cases for the functions exp_eval, infix_to_postifx, and
    the error handling functions embedded within those functions: infix_valid
    and postfix_valid.

Course:
    CPE202 section 07

Quarter:
    Winter 2019

Assignment:
    Project 2

Author:
    JeanReno Racines (jracines@calpoly.edu)
'''


import unittest
from exp_eval import infix_to_postfix
from exp_eval import postfix_eval


class TestCase(unittest.TestCase):
    '''A class to test the functions within exp_eval.
    '''
    def test_exp_eval1(self):
        '''A method to test the infix_to_postfix, infix_valid, postfix_eval,
            and the postfix_valid function.
        '''
        infix = '( ( 5 - 3 ) ^ 2 + ( 4 - 2 ) ^ 2 ) ^ ( 1 / 2 )'
        postfix = '5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertAlmostEqual(postfix_eval(postfix), 2.82842712475, 11)

    def test_exp_eval2(self):
        infix = '( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )'
        postfix = '15 7 1 1 + - / 3 * 2 1 1 + + -'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 5.0)

    def test_exp_eval3(self):
        infix = '10 + 3 * 5 / ( 16 - 4 )'
        postfix = '10 3 5 * 16 4 - / +'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 11.25)

    def test_exp_eval4(self):
        infix = '5 * 3 ^ ( 4 - 2 )'
        postfix = '5 3 4 2 - ^ *'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 45)

    def test_exp_eval5(self):
        infix = '( ( 1 * 2 ) + ( 3 / 4 ) )'
        postfix = '1 2 * 3 4 / +'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 2.75)

    def test_exp_eval6(self):
        infix = '( ( 2 * ( 3 + 4 ) ) / 5 )'
        postfix = '2 3 4 + * 5 /'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 2.8)

    def test_exp_eval7(self):
        infix = '( 3 * ( 4 + 6 / 3 ) )'
        postfix = '3 4 6 3 / + *'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 18)

    def test_exp_eval8(self):
        infix = '~ 3 * 3 + 9'
        postfix = '3 ~ 3 * 9 +'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 0)

    def test_exp_eval9(self):
        infix = '( ~ 3 ) ^ 2 + 9'
        postfix = '3 ~ 2 ^ 9 +'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 18)

    def test_exp_eval10(self):
        infix = '~ 3 ^ 2 + 9'
        postfix = '3 2 ^ ~ 9 +'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 0)

    def test_exp_eval11(self):
        infix = '4 ^ ( ~ 1 ) * 4'
        postfix = '4 1 ~ ^ 4 *'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 1)

    def test_exp_eval12(self):
        infix = '1'
        postfix = '1'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 1)

    def test_exp_eval13(self):
        infix = '4 ^ 2 ^ 2'
        postfix = '4 2 2 ^ ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 256)

    def test_exp_eval14(self):
        infix = '~ ( ~ 3 ) ^ 2 ^ 2 + 9'
        postfix = '3 ~ 2 2 ^ ^ ~ 9 +'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), -72)

    def test_exp_eval15(self):
        infix = '~ 3 ^ 2'
        postfix = '3 2 ^ ~'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), -9)

    def test_exp_eval16(self):
        infix = '( ~ 3 ) ^ 2'
        postfix = '3 ~ 2 ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 9)

    def test_exp_eval17(self):
        infix = '( ~ 3 ) ^ 2 ^ 2'
        postfix = '3 ~ 2 2 ^ ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 81)

    def test_exp_eval18(self):
        infix = '( ~ 3 ) ^ 3'
        postfix = '3 ~ 3 ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), -27)

    def test_exp_eval19(self):
        infix = '( ~ ~ 3 ) ^ 3'
        postfix = '3 ~ ~ 3 ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 27)

    def test_exp_eval20(self):
        infix = '~ ~ 3 ^ 3'
        postfix = '3 3 ^ ~ ~'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 27)

    def test_exp_eval21(self):
        infix = '2 ^ 3'
        postfix = '2 3 ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 8)

    def test_exp_eval22(self):
        infix = '3 ^ 2'
        postfix = '3 2 ^'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 9)

    def test_exp_eval23(self):
        infix = '2 * 3 ^ 2'
        postfix = '2 3 2 ^ *'
        self.assertAlmostEqual(postfix_eval(postfix), postfix_eval(infix_to_postfix(infix)))
        self.assertEqual(postfix_eval(postfix), 18)

    def test_errors58(self):
        postfix = '2 0 /'
        self.assertRaises(ZeroDivisionError, postfix_eval, postfix)

    def test_errors59(self):
        postfix = '2 2 2 ~ + /'
        self.assertRaises(ZeroDivisionError, postfix_eval, postfix)


def main():
    '''Execute unit tests
    '''
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()
