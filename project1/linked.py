""" Contains linked list implementations for project1
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


class LinkedList:
    """ The Linked List containing all the nodes; acts as the head.

    Attributes:
        head(Node): If the head of the node.
        num_items(int): The number of items in the linked list.
    """

    def __init__(self, head=Node(None)):
        self.head = head
        if self.head.get_data() is None:
            self.num_items = 0
        else:
            self.num_items = 1

    def __repr__(self):
        return "LinkedList({})".format(self.head)

    def __eq__(self, other):
        return (self.head == other.head and
                isinstance(self, LinkedList) == isinstance(other, LinkedList))

    def push(self, item):
        """ Add another Node to the linked list.

        Args:
            self(LinkedList): The current object referencing this method.
            item(*): Item that should be added to the linked list.

        Returns:
            None: Does not return anything.
        """
        if self.head.get_data() is None:
            self.head.set_data(item)
            self.num_items += 1
        else:
            new_node = Node(item)
            new_node.set_next(self.head)
            self.head = new_node
            self.num_items += 1

    def pop(self):
        """ remove a Node from the linked list.

        Args:
            self(LinkedList): The current object referencing this method.

        Returns:
            *: The item removed from the linked list.
        """
        if self.size() == 1:
            item = self.head.get_data()
            self.head.set_data(None)
            self.num_items -= 1
            return item
        item = self.head.get_data()
        self.head = self.head.get_next()
        self.num_items -= 1
        return item

    def is_empty(self):
        """ Checks if the linked list is empty or not.

        Args:
            self(LinkedList): The current object referencing this method.

        Returns:
            *: The item removed from the linked list.
        """
        return self.size() == 0

    def size(self):
        """ Returns the size of the linked list, in other words how many nodes
        there are in the linked list.

        Args:
            self(LinkedList): The current object referencing this method.

        Returns:
            *: The item removed from the linked list.
        """
        return self.num_items

    def reverse(self):
        """ Reverses the linked list.
        """
        if self.size() <= 1:
            return
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev