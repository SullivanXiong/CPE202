import unittest
from queues import QueueArray
from queues import QueueLinked


class TestCase(unittest.TestCase):

    def test_QueueArray(self):
        queue = QueueArray(2)
        self.assertRaises(IndexError, queue.dequeue)
        self.assertEqual(queue.is_empty(), True)
        queue.enqueue(1)
        self.assertEqual(queue.size(), 1)
        queue.enqueue(2)
        self.assertRaises(IndexError, queue.enqueue, 3)
        self.assertEqual(queue.is_full(), True)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)
        queue.enqueue(4)

    def test_QueueLinked(self):
        queue = QueueLinked(2)
        self.assertRaises(IndexError, queue.dequeue)
        self.assertEqual(queue.is_empty(), True)
        queue.enqueue(1)
        self.assertEqual(queue.size(), 1)
        queue.enqueue(2)
        self.assertRaises(IndexError, queue.enqueue, 3)
        self.assertEqual(queue.is_full(), True)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)


def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()