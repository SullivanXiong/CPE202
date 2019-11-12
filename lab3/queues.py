""" Contains Queue implementation for lab 3
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""


class Node:
    """ An data structure that stores a data the next Node object

    Attributes:
        data(*): The data that will be stored in this Node. Can be any data
                 type.
        next(Node): The next Node if it exist, else None.
    """

    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt

    def __repr__(self):
        return "Node({}, {})".format(self.data, self.next)

    def __eq__(self, other):
        return (self.data == other.data and
                self.next == other.next and
                isinstance(self, Node) == isinstance(other, Node))

    def get_data(self):
        """ Returns the data.

        Args:
            self(Node): The current object referencing this method.

        Returns:
            *: The data.
        """
        return self.data

    def set_data(self, new_data):
        """ Set the data to something else.

        Args:
            self(Node): The current object referencing this method.
            new_data(*): The new data.
        """
        self.data = new_data

    def get_next(self):
        """ Returns the data.

        Args:
            self(Node): The current object referencing this method.

        Returns:
            Node: The next Node or None.
        """
        return self.next

    def set_next(self, new_next):
        """ Set the next to something else.

        Args:
            self(Node): The current object referencing this method.
            new_next(Node): Set the next attribute to a new Node or None.
        """
        self.next = new_next


class QueueArray:
    """ A Queue implemented with the built in list. Mimics a circular array.

    Attributes:
        capacity(int): The size limit of the queue.
        front(int): Enqueue pointer.
        rear(int): Dequeue pointer.
        items(list): The list that serves as our queue.
        num_items(int): The number of items currently in the Queue.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def __repr__(self):
        return "QueueArray({}, {}, {}, {}, {})".format(self.capacity,
                                                       self.front,
                                                       self.rear,
                                                       self.items,
                                                       self.num_items)

    def __eq__(self, other):
        return (isinstance(self) == isinstance(other) and
                self.capacity == other.capacity and
                self.front == other.front and
                self.rear == other.rear and
                self.items == other.items and
                self.num_items == other.num_items)

    def is_empty(self):
        """ Checks if the queue is empty.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            bool: True if empty, else False.
        """
        return self.front == self.rear

    def is_full(self):
        """ Checks if the queue is full.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            bool: True if full, else False
        """
        return self.rear == (self.front + 1) % (self.capacity + 1)

    def enqueue(self, item):
        """ Adds a node to the end of the queue.

        Args:
            self(QueueArray): The current object referencing this method.
            item(*): The item being added to the queue.

        Returns:
            None: Does not return anything.

        Raises:
            IndexError: If the queue is full raises an error.
        """
        if self.is_full():
            raise IndexError
        if self.is_empty():
            self.items[self.front] = item
            self.front = (self.front + 1) % (self.capacity + 1)
            self.num_items += 1
        else:
            self.items[self.front] = item
            self.front = (self.front + 1) % (self.capacity + 1)
            self.num_items += 1

    def dequeue(self):
        """ Removes the node at the front of the queue.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            *: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty raises an error.
        """
        if self.is_empty():
            raise IndexError
        item = self.items[self.rear]
        self.rear = (self.rear + 1) % (self.capacity + 1)
        self.num_items -= 1
        return item

    def size(self):
        """ The number of items currently in the queue.

        Args:
            self(QueueArray): The current object referencing this method.

        Returns:
            int: Number of items currently in the queue.
        """
        return self.num_items


class QueueLinked:
    """ A Queue implemented with a Linked List.

    Attributes:
        capacity(int): The size limit of the queue.
        front(Node): Enqueue pointer, if empty it's None.
        rear(Node): Dequeue pointer, if empty it's None.
        num_items(int): The number of items currently in the Queue.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.num_items = 0

    def __repr__(self):
        return "QueueLinked({}, {}, {}, {})".format(self.capacity,
                                                    self.front,
                                                    self.rear,
                                                    self.num_items)

    def __eq__(self, other):
        return (isinstance(self) == isinstance(other) and
                self.capacity == other.capacity and
                self.front == other.front and
                self.rear == other.rear and
                self.num_items == other.num_items)

    def is_empty(self):
        """ Checks if the queue is empty.

        Args:
            self(QueueLinked): The current object referencing this method.

        Returns:
            bool: True if empty, else False.
        """
        return self.num_items == 0

    def is_full(self):
        """ Checks if the queue is full.

        Args:
            self(QueueLinked): The current object referencing this method.

        Returns:
            bool: True if full, else False
        """
        return self.num_items == self.capacity

    def enqueue(self, item):
        """ Adds a node to the end of the queue.

        Args:
            self(QueueLinked): The current object referencing this method.
            item(*): The item being added to the queue.

        Returns:
            None: Does not return anything.

        Raises:
            IndexError: If the queue is full raise an error.
        """
        if self.is_full():
            raise IndexError
        if self.is_empty():
            self.front = Node(item)
            self.rear = self.front
            self.num_items += 1
        else:
            self.front.set_next(Node(item))
            self.front = self.front.next
            self.num_items += 1

    def dequeue(self):
        """ Removes the node at the front of the queue.

        Args:
            self(QueueLinked): The current object referencing this method.

        Returns:
            *: The item at the rear of the queue.

        Raises:
            IndexError: If the queue is empty raise an error.
        """
        if self.is_empty():
            raise IndexError
        if self.size() == 1:
            item = self.rear.get_data()
            self.front = None
            self.rear = None
            self.num_items -= 1
            return item
        item = self.rear.get_data()
        self.rear = self.rear.next
        self.num_items -= 1
        return item

    def size(self):
        """ The number of items currently in the queue.

        Args:
            self(QueueLinked): The current object referencing this method.

        Returns:
            int: Number of items currently in the queue.
        """
        return self.num_items
