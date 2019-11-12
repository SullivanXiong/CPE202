""" Contains stack implementations for project1
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""
from linked import LinkedList


class StackArray:
    """ A stack data structure implemented with the built in list data type.

    Attributes:
        capacity(int): The size limiter of the stack.
        items(list): A list containing the data of the items and None.
        num_items(int): The number of items in the stack.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0

    def __repr__(self):
        return "StackArray({}, {}, {})".format(self.capacity, self.items, self.num_items)

    def __eq__(self, other):
        return (isinstance(self, StackArray) ==
                isinstance(other, StackArray) and
                self.capacity == other.capacity and
                self.items == other.items and
                self.num_items == other.num_items)

    def is_empty(self):
        """ Checks if the stack is empty.

        Args:
            self(StackArray): The current object referencing this method.

        Returns:
            boolean: True if the stack is empty, else false.
        """
        return self.num_items == 0

    def is_full(self):
        """ Checks if the stack is full.

        Args:
            self(StackArray): The current object referencing this method.

        Returns:
            boolean: True if the stack is full, else false.
        """
        return self.num_items == self.capacity

    def push(self, item):
        """ Add an item to the stack. If the stack is full return Error.

        Args:
            self(StackArray): The current object referencing this method.
            item(Any): The data that is going to be pushed to the stack

        Returns:
            None: Does not return anything
        """
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self):
        """ Removes an item from the top of the stack. If the stack is empty
        return None.

        Args:
            self(StackArray): The current object referencing this method.

        Returns:
            Any: The data that was removed from the top of the stack.
        """
        if self.is_empty():
            raise IndexError
        item = self.items[self.num_items-1]
        self.items[self.num_items-1] = None
        self.num_items -= 1
        return item

    def peek(self):
        """ The item at the top of the Stack.

        Args:
            self(StackArray): The current object referencing this method.

        Returns:
            *: The data at the top of the Stack.
        """
        return self.items[self.num_items-1]

    def size(self):
        """ The size of the StackArray.

        Args:
            self(StackArray): The current object referencing this method.

        Returns:
            int: Number of items in the Stack.
        """
        return self.num_items


class StackLinked:
    """ A stack data structure implemented with a singly linked list.

    Attributes:
        capacity(int): The size limiter of the stack.
        head(LinkedList): The LinkedList that stores our nodes.
        num_items(int): The number of items in the stack.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = LinkedList()
        self.num_items = 0

    def __repr__(self):
        return "StackLinked({}, {}, {})".format(self.capacity,
                                                self.items,
                                                self.num_items)

    def __eq__(self, other):
        return (isinstance(self, StackLinked) ==
                isinstance(other, StackLinked) and
                self.capacity == other.capacity and
                self.items == other.items and
                self.num_items == other.num_items)

    def is_empty(self):
        """ Checks if the stack is empty.

        Args:
            self(StackLinked): The current object referencing this method.

        Returns:
            boolean: True if the stack is empty, else false.
        """
        return self.num_items == 0

    def is_full(self):
        """ Checks if the stack is full.

        Args:
            self(StackLinked): The current object referencing this method.

        Returns:
            boolean: True if the stack is full, else false.
        """
        return self.num_items == self.capacity

    def push(self, item):
        """ Add an item to the stack. If the stack is full return Error.

        Args:
            self(StackLinked): The current object referencing this method.
            item(Any): The data that is going to be pushed to the stack

        Returns:
            None: Does not return anything
        """
        if self.is_full():
            raise IndexError
        self.items.push(item)
        self.num_items += 1

    def pop(self):
        """ Removes an item from the top of the stack. If the stack is empty
        return None.

        Args:
            self(StackLinked): The current object referencing this method.

        Returns:
            Any: The data that was removed from the top of the stack.
        """
        if self.is_empty():
            raise IndexError
        self.num_items -= 1
        return self.items.pop()

    def peek(self):
        """ The item at the top of the Stack.

        Args:
            self(StackLinked): The current object referencing this method.

        Returns:
            *: The data at the top of the Stack.
        """
        return self.items.head.get_data()

    def size(self):
        """ The size of the StackLinked.

        Args:
            self(StackLinked): The current object referencing this method.

        Returns:
            int: Number of items in the Stack.
        """
        return self.items.num_items
