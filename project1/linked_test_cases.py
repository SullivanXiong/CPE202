import unittest
from linked import Node
from linked import LinkedList


class TestCase(unittest.TestCase):

    def test_Node(self):
        node1 = Node('data')
        node1.data
        #node1.data
        self.assertEqual(node1.data, 'data')
        node2 = Node('data2')
        node1.next = node2
        #node1.next.data
        self.assertEqual(node1.next.data, 'data2')

    def test_LinkedList(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.size(), 0)
        linked_list_num = LinkedList(Node(1))
        self.assertEqual(linked_list_num.pop(), 1)
        self.assertEqual(linked_list_num.push(1), None)
        self.assertEqual(linked_list_num.head.data, 1)
        self.assertEqual(linked_list_num.head.next, None)
        self.assertEqual(linked_list_num.push(2), None)
        self.assertEqual(linked_list_num.pop(), 2)
        self.assertEqual(linked_list_num.size(), 1)
        self.assertEqual(linked_list_num.is_empty(), False)

    def test_LinkedList_reverse(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        print(repr(linked_list))
        linked_list.reverse()
        print(repr(linked_list))
        

def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()