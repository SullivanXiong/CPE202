""" Contains the classes for LinkedList implementation of lab 7
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""

class Node:
    """ Node implementation
    Attributes:
        data (*) : The data stored in the Node
        next (Node) : The connection to the next Node, otherwise None
    """
    
    def __init__(self, key, data, nxt=None):
        self.key = key
        self.data = data
        self.next = nxt
    
    def __repr__(self):
        return "Node({}, {})".format(self.data, self.next)

    def __eq__(self, other):
        return isinstance(other, Node)\
            and self.data == other.data\
            and self.next == other.next
    
    def get_key(self):
        """ Returns the key.

        Args:
            self(Node): The current object referencing this method.

        Returns:
            *: The key.
        """
        return self.key

    def set_key(self, new_key):
        """ Set the key to something else.

        Args:
            self(Node): The current object referencing this method.
            new_key(*): The new key.
        """
        self.key = new_key

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
    """ The implementation of LinkedList with Node class
    Attributes:
        head (Node) : The head of the node
        num_items (int) : The number of items in the linked list
    """

    def __init__(self, head=None):
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

    def push(self, key, data):
        """ Add another Node to the linked list.

        Args:
            self(LinkedList): The current object referencing this method.
            item(*): Item that should be added to the linked list.

        Returns:
            None: Does not return anything.
        """
        if self.head.get_data() is None:
            self.head.set_key(key)
            self.head.set_data(data)
            self.num_items += 1
        else:
            new_node = Node(key, data)
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
            item = (self.head.get_key(), self.head.get_data())
            self.head.set_key(None)
            self.head.set_data(None)
            self.num_items -= 1
            return item
        item = (self.head.get_key(), self.head.get_data())
        self.head = self.head.get_next()
        self.num_items -= 1
        return item

    def remove(self, key):
        head = self.head
        prev = self.head
        nxt = self.head.next
        if head.key == key:
            item = (head.get_key(), head.get_data())
            self.head = head.get_next()
            self.num_items -= 1
            return item
        head = head.next
        nxt = nxt.next
        while nxt != None:
            if head.key == key:
                item = (head.get_key(), head.get_data())
                head.next = None
                prev.next = nxt
                self.head = head.get_next()
                self.num_items -= 1
                return item
            prev = prev.next
            head = head.next
            nxt = nxt.next
        if head.key == key:
            item = (head.get_key(), head.get_data())
            prev.next = nxt
            self.head = prev
            self.num_items -= 1
            return item
        return None

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