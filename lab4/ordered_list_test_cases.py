import unittest
from ordered_list import Node
from ordered_list import OrderedList

class TestCase(unittest.TestCase):

    def test_OrderedList(self):
        ordered_list = OrderedList()
        self.assertEqual(ordered_list.is_empty(), True)
        ordered_list.add(2)
        ordered_list.add(1)
        ordered_list.add(3)
        self.assertEqual(ordered_list.size(), 3)
        self.assertEqual(ordered_list.index(2), 1)
        self.assertEqual(ordered_list.index(4), -1)
        self.assertEqual(ordered_list.search_forward(3), True)
        self.assertEqual(ordered_list.search_backward(3), True)
        self.assertEqual(ordered_list.remove(4), -1)
        self.assertEqual(ordered_list.remove(2), 1)
        self.assertEqual(ordered_list.pop(0), 1)
        self.assertEqual(ordered_list.pop(), 3)

    def test_OrderedList_coverage_cases(self):
        ordered_list = OrderedList()
        ordered_list.add(1)
        ordered_list.add(2)
        ordered_list.add(5)
        ordered_list.add(3)
        self.assertEqual(ordered_list.search_forward(4), False)
        self.assertEqual(ordered_list.search_forward(6), False)
        self.assertEqual(ordered_list.search_forward(1), True)
        self.assertEqual(ordered_list.search_backward(4), False)
        self.assertEqual(ordered_list.search_backward(2), True)
        self.assertEqual(ordered_list.search_backward(5), True)
        self.assertEqual(ordered_list.pop(), 5)
        self.assertEqual(ordered_list.pop(1), 2)
        self.assertEqual(ordered_list.pop(), 3)
        self.assertRaises(IndexError, ordered_list.pop, 1)
        self.assertEqual(ordered_list.index(1), 0)
        self.assertEqual(ordered_list.pop(), 1)
        self.assertRaises(IndexError, ordered_list.pop)

    def test_OrderedList_office_hours(self):
        orderlst = OrderedList()
        orderlst.add(5)
        orderlst.add(3)
        orderlst.add(6)
        orderlst.add(2)
        self.assertEqual(orderlst.pop(),6)
        self.assertEqual(orderlst.pop(0), 2)


def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()