import unittest
from lab1 import get_max
from lab1 import reverse
from lab1 import search
from lab1 import fib
from lab1 import factorial_iter
from lab1 import factorial_rec

class TestCase(unittest.TestCase):
    def test_get_max(self):
        arr = [1,2,3,4,5]
        self.assertEqual(get_max(arr), 5)
        arr = []
        self.assertEqual(get_max(arr), None)
        arr = [1, 2, 4, 7, 3, 10, 9, 6]
        self.assertEqual(get_max(arr), 10)
        arr = [5]
        self.assertEqual(get_max(arr), 5)


    def test_reverse(self):
        self.assertEqual(reverse("qweEerty"), "ytreEewq")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("$3.29"), "92.3$")
        self.assertEqual(reverse("   _Sullivan_Xiong_"), "_gnoiX_navilluS_   ")


    def test_search(self):
        arr = [1,2,3,4,5]
        self.assertEqual(search(arr, 5), 4)
        arr = []
        self.assertEqual(search(arr, 5), None)
        arr = [2, 4, 6, 8, 10, 12, 14, 16]
        self.assertEqual(search(arr, 10), 4)
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(search(arr, 2), 1)
        self.assertEqual(search(arr, 8), None)


    def test_fib(self):
        def fib_numbers(n):
            sequence = []
            for i in range(n+1):
                sequence.append(fib(i))
            return sequence 

        #this will test your fib function by calling it multiple times
        self.assertEqual(fib_numbers(10),
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(fib_numbers(0),
                         [0])
        self.assertEqual(fib_numbers(1),
                         [0, 1])
        self.assertEqual(fib_numbers(2),
                         [0, 1, 1])
        self.assertEqual(fib_numbers(12),
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])


    def test_factorial(self):
        self.assertEqual(factorial_iter(3), 6)
        self.assertEqual(factorial_iter(3), factorial_rec(3))
        self.assertEqual(factorial_iter(20), factorial_rec(20))
        self.assertEqual(factorial_rec(4), 24)


def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()
