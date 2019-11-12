import unittest
from linked import Node
from stacks import StackArray
from stacks import StackLinked


class TestCase(unittest.TestCase):
    
    def test_Node(self):
        node1 = Node('data')
        self.assertEqual(node1.data, 'data')
        node2 = Node('data2')
        node1.next = node2
        self.assertEqual(node1.next.data, 'data2')

    def test_StackArray(self):
        stack = StackArray(3)
        self.assertRaises(IndexError, stack.pop)
        self.assertEqual(stack.is_empty(), True)
        stack.push('book1')
        stack.push('book2')
        self.assertEqual(stack.peek(), 'book2')
        self.assertEqual(stack.pop(), 'book2')
        self.assertEqual(stack.peek(), 'book1')
        stack.push('book2_2')
        stack.push('book3')
        self.assertRaises(IndexError, stack.push, 'book4')
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.is_full(), True)

    def test_StackLinked(self):
        stack = StackLinked(3)
        self.assertRaises(IndexError, stack.pop)
        self.assertEqual(stack.is_empty(), True)
        stack.push('book1')
        self.assertEqual(stack.pop(), 'book1')
        stack.push('book1')
        stack.push('book2')
        self.assertEqual(stack.peek(), 'book2')
        self.assertEqual(stack.pop(), 'book2')
        self.assertEqual(stack.peek(), 'book1')
        stack.push('book2_2')
        stack.push('book3')
        self.assertRaises(IndexError, stack.push, 'book4')
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.is_full(), True)
        
def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()