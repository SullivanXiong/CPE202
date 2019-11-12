""" Contains the classes for LinkedList implementation of lab 7
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""

from linked_lists import *


class HashTableSepchain:
    """ Hashtable implemented with the collision solution
    Separate Chaining
    Attributes:
        hash_table (list) : The list the stores the data of the hashtable
        table_size (int) : The len of the hash_table, default 11
        num_items (int) : The number of items in the hashtable
        collision (int) : The number of collisions that has in the hashtable
    """

    def __init__(self, table_size=11):
        self.hash_table = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.collision = 0

    def __repr__(self):
        return "HashTableSepchain({}, {})".format(self.hash_table, self.table_size)

    def __eq__(self, other):
        return isinstance(other, HashTableQuadratic)\
            and self.hash_table == other.hash_table\
            and self.table_size == other.table_size\
            and self.num_items == other.num_items\
            and self.collision == other.collision

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """insert a key-value pair into the hashtable using the key as the hash
        value generated with hash_string()
        Args:
            key (str) : The key
            data (*) : The corresponding value pair
        """
        hash_value = hash_string(key, self.table_size)
        new_node = Node(key, data)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = LinkedList(new_node)
            self.num_items += 1
        else:
            end = self.hash_table[hash_value].head
            while end.next is not None:
                end = end.next
            end.next = new_node
            self.num_items += 1
            self.collision += 1
        if self.load_factor() > 1.5:
            old_hash_table = self.hash_table[:]
            self.table_size = self.table_size * 2 + 1
            self.hash_table = [None] * self.table_size
            self.num_items = 0
            self.collision = 0
            for item in old_hash_table:
                if item is not None:
                    nxt = item.head
                    while nxt is not None:
                        hash_value = hash_string(nxt.key, self.table_size)
                        new_node = Node(nxt.key, nxt.key)
                        if self.hash_table[hash_value] is None:
                            self.hash_table[hash_value] = LinkedList(new_node)
                            self.num_items += 1
                        else:
                            end = self.hash_table[hash_value].head
                            while end.next is not None:
                                end = end.next
                            end.next = new_node
                            self.num_items += 1
                            self.collision += 1
                        nxt = nxt.next

    def get(self, key):
        """search the hashtable to see if the key exists in the hashtable then
        return the data pair associated with the key
        Args:
            key (str) : The key
        Returns:
            * : The data pair corresponding with the given key
        """
        item = self.hash_table[hash_string(key, self.table_size)]
        if item.head is None:
            raise LookupError
        end = item.head
        while end.key is not None:
            if end.key == key:
                return end.data
            end = end.next
        raise LookupError

    def contains(self, key):
        """search the hashtable to see if the key exists in the hashtable
        Args:
            key (str) : The key
        Returns:
            bool : True if the hashtable contains the key.
        """
        try:
            self.get(key)
            return True
        except LookupError:
            return False

    def remove(self, key):
        """remove the data with the given key from the hashtable
        Args:
            key (str) : The key
        Returns:
            * : The data that was removed from the hashtable
        """
        hash_value = hash_string(key, self.table_size)
        item = self.hash_table[hash_value].remove(key)
        if item is not None:
            self.collision -= 1
        return item

    def size(self):
        """ The number of items in the hashtable
        Returns:
            int : The number of items in the hashtable
        """
        return self.num_items

    def load_factor(self):
        """the load factor value of the hashtable
        Returns:
            float : The current load factor of the hashtable
        """
        return self.size() / self.table_size

    def collisions(self):
        """the number of collisions that the hashtable encountered
        Returns:
            int : The number of collisions
        """
        return self.collision


class HashTableLinear:
    """ Hashtable implemented with the collision solution
    Linear Open Addressing
    Attributes:
        hash_table (list) : The list the stores the data of the hashtable
        table_size (int) : The len of the hash_table, default 11
        num_items (int) : The number of items in the hashtable
        collision (int) : The number of collisions that has in the hashtable
    """

    def __init__(self, table_size=11):
        self.hash_table = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.collision = 0

    def __repr__(self):
        return "HashTableLinear({}, {})".format(self.hash_table, self.table_size)

    def __eq__(self, other):
        return isinstance(other, HashTableQuadratic)\
            and self.hash_table == other.hash_table\
            and self.table_size == other.table_size\
            and self.num_items == other.num_items\
            and self.collision == other.collision

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """insert a key-value pair into the hashtable using the key as the hash
        value generated with hash_string()
        Args:
            key (str) : The key
            data (*) : The corresponding value pair
        """
        hash_value = hash_string(key, self.table_size)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = data
            self.num_items += 1
        elif self.hash_table[hash_value] == key:
            self.hash_table[hash_value] = data
        else:
            i = 1
            self.collision += 1
            while self.hash_table[(hash_value + i) % self.table_size] is not None:
                i += 1
                self.collision += 1
            self.hash_table[(hash_value + i) % self.table_size] = data
            self.num_items += 1
        if self.load_factor() > 0.75:
            copy_hash_table = self.hash_table[:]
            self.table_size = self.table_size * 2 + 1
            self.hash_table = [None] * self.table_size
            self.collision = 0
            self.num_items = 0
            for item in copy_hash_table:
                if item is not None:
                    hash_value = hash_string(item, self.table_size)
                    if self.hash_table[hash_value] is None:
                        self.hash_table[hash_value] = item
                        self.num_items += 1
                    elif self.hash_table[hash_value] == key:
                        self.hash_table[hash_value] = item
                    else:
                        i = 1
                        self.collision += 1
                        while self.hash_table[(hash_value + i) % self.table_size] is not None:
                            i += 1
                            self.collision += 1
                        self.hash_table[(hash_value + i) %
                                        self.table_size] = item
                        self.num_items += 1

    def get(self, key):
        """search the hashtable to see if the key exists in the hashtable then
        return the data pair associated with the key
        Args:
            key (str) : The key
        Returns:
            * : The data pair corresponding with the given key
        """
        hash_value = hash_string(key, self.table_size)
        i = 0
        while self.hash_table[hash_value + i] is not None:
            if self.hash_table[hash_value + i] == key:
                return hash_value + i
            i += 1
        raise LookupError

    def contains(self, key):
        """search the hashtable to see if the key exists in the hashtable
        Args:
            key (str) : The key
        Returns:
            bool : True if the hashtable contains the key.
        """
        try:
            self.get(key)
            return True
        except LookupError:
            return False

    def remove(self, key):
        """remove the data with the given key from the hashtable
        Args:
            key (str) : The key
        Returns:
            * : The data that was removed from the hashtable
        """
        hash_value = hash_string(key, self.table_size)
        i = 0
        collided = 0
        while self.hash_table[hash_value + i] is not None:
            if self.hash_table[hash_value + i] == key:
                return_item = (key, self.hash_table[hash_value + i])
                self.hash_table[hash_value + i] = None
                self.num_items -= 1
                hash_value = hash_value + i + 1
                if collided > 0:
                    self.collision -= collided
                    collided = 0
                while self.hash_table[hash_value] is not None:
                    item = self.hash_table[hash_value]
                    new_hash_val = hash_string(item, self.table_size)
                    if self.hash_table[new_hash_val] is None:
                        self.hash_table[new_hash_val] = item
                        self.hash_table[hash_value] = None
                        collided = 1
                    elif self.hash_table[new_hash_val] == item:
                        self.hash_table[new_hash_val] = item
                    else:
                        k = 1
                        self.collision -= 1
                        while self.hash_table[(new_hash_val + k) % self.table_size] is not None:
                            k += 1
                            self.collision -= 1
                        self.hash_table[(new_hash_val + k) %
                                        self.table_size] = item
                        self.hash_table[hash_value] = None
                    if collided > 0:
                        self.collision -= collided
                        collided = 0
                    hash_value += 1
                return return_item
            i += 1
            collided += 1

    def size(self):
        """the load factor value of the hashtable
        Returns:
            float : The current load factor of the hashtable
        """
        return self.num_items

    def load_factor(self):
        """the load factor value of the hashtable
        Returns:
            float : The current load factor of the hashtable
        """
        return self.size() / self.table_size

    def collisions(self):
        """the number of collisions that the hashtable encountered
        Returns:
            int : The number of collisions
        """
        return self.collision


class HashTableQuadratic:
    """ Hashtable implemented with the collision solution
    Quadratic Open Addressing
    Attributes:
        hash_table (list) : The list the stores the data of the hashtable
        table_size (int) : The len of the hash_table, default 11
        num_items (int) : The number of items in the hashtable
        collision (int) : The number of collisions that has in the hashtable
    """

    def __init__(self, table_size=11):
        self.hash_table = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.collision = 0

    def __repr__(self):
        return "HashTableQuadratic({}, {})".format(self.hash_table, self.table_size)

    def __eq__(self, other):
        return isinstance(other, HashTableQuadratic)\
            and self.hash_table == other.hash_table\
            and self.table_size == other.table_size\
            and self.num_items == other.num_items\
            and self.collision == other.collision

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        return self.contains(key)

    def put(self, key, data):
        """insert a key-value pair into the hashtable using the key as the hash
        value generated with hash_string()
        Args:
            key (str) : The key
            data (*) : The corresponding value pair
        """
        hash_value = hash_string(key, self.table_size)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = data
            self.num_items += 1
        elif self.hash_table[hash_value] == key:
            self.hash_table[hash_value] = key
        else:
            i = 1
            hash_value = hash_value + (i ** 2)
            self.collision += 1
            while self.hash_table[hash_value % self.table_size] is not None:
                i += 1
                hash_value = hash_value + (i ** 2)
                self.collision += 1
            self.hash_table[hash_value % self.table_size] = data
            self.num_items += 1
        if self.load_factor() > .75:
            copy_hash_table = self.hash_table[:]
            self.table_size = self.table_size * 2 + 1
            self.hash_table = [None] * self.table_size
            self.collision = 0
            self.num_items = 0
            for item in copy_hash_table:
                if item is not None:
                    hash_value = hash_string(item, self.table_size)
                    if self.hash_table[hash_value] is None:
                        self.hash_table[hash_value] = item
                        self.num_items += 1
                    elif self.hash_table[hash_value] == key:
                        self.hash_table[hash_value] = item
                    else:
                        i = 1
                        hash_value = hash_value + (i ** 2)
                        self.collision += 1
                        while self.hash_table[hash_value % self.table_size] is not None:
                            i += 1
                            hash_value = hash_value + (i ** 2)
                            self.collision += 1
                        self.hash_table[hash_value % self.table_size] = item
                        self.num_items += 1

    def get(self, key):
        """search the hashtable to see if the key exists in the hashtable then
        return the data pair associated with the key
        Args:
            key (str) : The key
        Returns:
            * : The data pair corresponding with the given key
        """
        hash_value = hash_string(key, self.table_size)
        i = 0
        while self.hash_table[hash_value] is not None:
            if self.hash_table[hash_value] == key:
                return hash_value + (i ** 2)
            i += 1
            hash_value = hash_value + (i ** 2)
        raise LookupError

    def contains(self, key):
        """search the hashtable to see if the key exists in the hashtable
        Args:
            key (str) : The key
        Returns:
            bool : True if the hashtable contains the key.
        """
        try:
            self.get(key)
            return True
        except LookupError:
            return False

    def remove(self, key):
        """remove the data with the given key from the hashtable
        Args:
            key (str) : The key
        Returns:
            * : The data that was removed from the hashtable
        """
        hash_value = hash_string(key, self.table_size)
        i = 0
        collided = 0
        while self.hash_table[hash_value] is not None:
            if self.hash_table[hash_value] == key:
                return_item = (key, self.hash_table[hash_value])
                self.hash_table[hash_value] = None
                self.num_items -= 1
                hash_value = hash_value + ((i + 1) ** 2)
                if collided > 0:
                    self.collision -= collided
                    collided = 0
                while self.hash_table[hash_value] is not None:
                    item = self.hash_table[hash_value]
                    new_hash_val = hash_string(item, self.table_size)
                    if self.hash_table[new_hash_val] is None:
                        self.hash_table[new_hash_val] = item
                        self.hash_table[hash_value] = None
                        collided = 1
                    elif self.hash_table[new_hash_val] == item:
                        self.hash_table[new_hash_val] = item
                    else:
                        k = 1
                        new_hash_val = new_hash_val + (k ** 2)
                        self.collision -= 1
                        while self.hash_table[(new_hash_val) % self.table_size] is not None:
                            k += 1
                            new_hash_val += new_hash_val + (k ** 2)
                            self.collision -= 1
                        self.hash_table[(new_hash_val) %
                                        self.table_size] = item
                        self.hash_table[hash_value] = None
                    if collided > 0:
                        self.collision -= collided
                        collided = 0
                    hash_value += 1
                return return_item
            i += 1
            hash_value = hash_value + (i ** 2)
            collided += 1

    def size(self):
        """the load factor value of the hashtable
        Returns:
            float : The current load factor of the hashtable
        """
        return self.num_items

    def load_factor(self):
        """the load factor value of the hashtable
        Returns:
            float : The current load factor of the hashtable
        """
        return self.size() / self.table_size

    def collisions(self):
        """the number of collisions that the hashtable encountered
        Returns:
            int : The number of collisions
        """
        return self.collision


def hash_string(string, size):
    """description
    Args:
    Returns:
    """
    hash_value = 0
    for char in string:
        hash_value = (hash_value * 31 + ord(char)) % size
    return hash_value

def import_stopwords(filename, hashtable):
    """reads from a file and creates a hashtable from it.
    Args:
        filename (str) : the name of the input file
        hashtable (HashTable*) : One of the three HashTable classes
    Returns:
        HashTable*: Updated hashtable with the input file's words inserted
    """
    with open(filename, "r") as input_file:
        lines = input_file.readlines().split()
        for line in lines:
            print(type(hashtable))
            for word in line:
                hashtable.put(word, word)
                print(hashtable.load_factor())
                print(len(hashtable.hash_table))
            return hashtable
