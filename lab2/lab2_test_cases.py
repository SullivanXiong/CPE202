import unittest
from lab2 import perm_lex

class TestCase(unittest.TestCase):
    def test_perm_lex(self):
        result = [
            'abcd',
            'abdc',
            'acbd',
            'acdb',
            'adbc',
            'adcb',
            'bacd',
            'badc',
            'bcad',
            'bcda',
            'bdac',
            'bdca',
            'cabd',
            'cadb',
            'cbad',
            'cbda',
            'cdab',
            'cdba',
            'dabc',
            'dacb',
            'dbac',
            'dbca',
            'dcab',
            'dcba'
        ]
        self.assertEqual(perm_lex("abcd"), result)
        result = ['CPE', 'CEP', 'PCE', 'PEC', 'ECP', 'EPC']
        self.assertEqual(perm_lex("CPE"), result)
        result = ['a']
        self.assertEqual(perm_lex("a"), result)
        result = []
        self.assertEqual(perm_lex(""), result)
        self.assertEqual(perm_lex(None), result)


def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()
