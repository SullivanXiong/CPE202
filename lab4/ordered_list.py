""" Contains OrderedList class and Node class
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

    def __init__(self, data, nxt=None, prev=None):
        self.data = data
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        return "Node({}, {})".format(self.get_data(), self.get_next())

    def __eq__(self, other):
        return (self.data == other.data and
                self.next == other.next and
                self.prev == other.prev and
                isinstance(self, Node) == isinstance(other, Node))

    def get_data(self):
        """ Returns the data.

        Args:

        Returns:
            *: The data.
        """
        return self.data

    def set_data(self, new_data):
        """ Set the data to something else.

        Args:
            new_data(*): The new data.
        """
        self.data = new_data

    def get_next(self):
        """ Returns the data.
        Returns:
            Node: The next Node or None.
        """
        return self.next

    def set_next(self, new_next):
        """ Set the next to something else.

        Args:
            new_next(Node): Set the next attribute to a new Node or None.
        """
        self.next = new_next

    def get_prev(self):
        """ Returns the previous node.
        Returns:
            Node: The next Node or None.
        """
        return self.prev

    def set_prev(self, new_prev):
        """ Set the data to something else.

        Args:
            new_next(Node): Set the next attribute to a new Node or None.
        """
        self.prev = new_prev


class OrderedList:
    """ An abstract data structure that links Nodes in a doubly linked
    list in ascending order.

    Attributes:
        head(Node): The first Node, smallest value of the list.
        tail(Node): The last Node, biggest value of the list.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __repr__(self):
        return "OrderedList({})".format(self.head)

    def __eq__(self, other):
        return (isinstance(self, OrderedList) ==
                isinstance(other, OrderedList) and
                self.head == other.head and
                self.tail == other.tail and
                self.num_items == other.num_items)

    def add(self, item):
        """ Adds a new item to the list in the correctly sorted position.

        Args:
            item(int): The item that is being added to the ordered list.
        """
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
            self.head = self.tail
            self.num_items += 1
        else:
            if item > self.head.get_data():
                curr = self.head
                while curr and item > curr.get_data():
                    curr = curr.next
                if curr is None:
                    new_node = Node(item)
                    self.tail.set_next(new_node)
                    new_node.set_prev(self.tail)
                    new_node.set_next(None)
                    self.tail = new_node
                    self.num_items += 1
                else:
                    new_node = Node(item)
                    nxt = curr
                    prev = curr.prev
                    prev.set_next(new_node)
                    nxt.set_prev(new_node)
                    new_node.set_next(curr)
                    new_node.set_prev(prev)
                    self.num_items += 1
            else:
                new_node = Node(item)
                new_node.set_prev(None)
                new_node.set_next(self.head)
                self.head.set_prev(new_node)
                self.head = new_node
                curr = self.head
                while curr.next:
                    curr = curr.next
                self.tail = curr
                self.num_items += 1

    def remove(self, item):
        """ Remove the Node with the corresponding item as its data.

        Args:
            item(int): The item that is being removed to the ordered list.
        Returns:
            int: Returns the position of the removed node, else if not found
                 returns -1.
        """
        pos = self.index(item)
        if pos == -1:
            return -1
        curr = self.head
        i = 0
        while i < pos:
            i += 1
            curr = curr.next
        prev = curr.prev
        nxt = curr.next
        prev.set_next(nxt)
        nxt.set_prev(prev)
        curr = None
        self.num_items -= 1
        return pos

    def search_forward(self, item):
        """ Searchs for the the item in the list starting from the head.

        Args:
            item(int): The item that is being searched for in the ordered list.
        Returns:
            boolean: Returns True if the item is in the list, else False.
        """
        curr = self.head
        if curr.get_data() == item:
            return True
        i = 0
        while i < self.size():
            i += 1
            if curr.get_data() == item:
                return True
            curr = curr.next
        return False

    def search_backward(self, item):
        """ Searchs for the the item in the list starting from the tail

        Args:
            item(int): The item that is being searched for in the ordered list.
        Returns:
            boolean: Returns True if the item is in the list, else False.
        """
        curr = self.tail
        if curr.get_data() == item:
            return True
        i = 0
        while i < self.size():
            i += 1
            if curr.get_data() is item:
                return True
            curr = curr.prev
        return False

    def is_empty(self):
        """ Checks if the ordered list is empty.

        Returns:
            boolean: Returns True if the ordered list is empty, else False.
        """
        return self.size() == 0

    def size(self):
        """ Returns the number of items in the list

        Returns:
            int: The number of items in the list.
        """
        return self.num_items

    def index(self, item):
        """ Search for the index of an item.

        Args:
            item(int): The item we are searching the index of.
        Returns:
            int: Returns the index of the item if found, else -1.
        """
        index = 0
        curr = self.head
        if curr.get_data() == item:
            return 0
        i = 0
        while i < self.size():
            i += 1
            if curr.get_data() == item:
                return index
            curr = curr.next
            index += 1
        return -1

    def pop(self, pos=None):
        """ Removes the Node at the given position, or if not given a position
        argument then remove the last node and return the item at that position
        if it exists.

        Args:
            pos(int): If the pos is defined, pop the Node at the nth position,
                      else pop the last item.
        Returns:
            int: The item at that position, else -1.
        """
        if self.head is None:
            raise IndexError
        elif pos is None:
            item = self.tail.get_data()
            prev = self.tail.prev
            if prev:
                prev.set_next(None)
            self.tail.set_prev(None)
            self.tail = prev
            if self.tail is None:
                self.head = None
            self.num_items -= 1
            return item
        curr = self.head
        i = 0
        while i < pos:
            i += 1
            curr = curr.next
            if curr is None:
                raise IndexError
        item = curr.get_data()
        prev = curr.get_prev()
        nxt = curr.get_next()
        if prev:
            prev.set_next(nxt)
            nxt.set_prev(prev)
            self.head = prev
        elif nxt:
            self.head = nxt
        else:
            self.head = None
            self.tail = self.head
        curr = None
        self.num_items -= 1
        return item
