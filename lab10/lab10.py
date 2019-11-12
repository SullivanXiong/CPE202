""" Contains starter code for lab 5
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""
import random

#implement BSTNode class and get,contains,insert,delete functions in bst.py
from bst_rb import BSTNode, get, contains, insert, delete, size
#classmate.py is implemented for you
from classmate import Classmate, classmate_factory


class TreeMap:
    """ Tree Map implemented with a binary search tree method.
    Attributes:
        tree (BSTNode): The root node of the Tree Map.
    """
    def __init__(self, tree=None):
        self.tree = tree

    def __repr__(self):
        #Complete this method
        return "TreeMap({})".format(self.tree)

    def __eq__(self, other):
        #Complete this method
        return isinstance(other, type(self))\
            and self.tree == other.tree

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.

        Args:
            key (str) : the key (last name)
        Returns:
            Classmate : an item associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.

        Args:
            key (str) : the key (last name)
            val (Classmate): a Classmate object.
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion

        Args:
            key (str) : the key (last name)

        Returns:
            bool : True is the key exists, otherwise False
        """
        return self.contains(key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py

        Args:
            key (str) : the key (last name)
            val (Classmate) : an object of Classmate
        """
        self.tree = insert(self.tree, key, val)

    def get(self, key):
        """Gets the value of the key by tranversing the BST tree map
        Calls get function in bst.py

        Args:
            key (str) : the key (last name)
        """
        return get(self.tree, key)

    def contains(self, key):
        """Checks to see if the key exists in the BST tree map
        Calls contains function in bst.py

        Args:
            key (str) : the key (last name)
        Returns:
            boolean: Returns true if the key exists in the in TreeMap.
        """
        return contains(self.tree, key)

    def delete(self, key):
        """Removes a BSTNode from the tree map with the corresponding key.
        Calls delete function in bst.py

        Args:
            key (str) : the key (last name).
        """
        self.tree = delete(self.tree, key)

    def size(self):
        """Returns the number of items in the map
        Calls size function in bst.py
        Returns:
            int: The number of nodes in the TreeMap.
        """
        return size(self.tree)

    # def search_range(self, from, to):
        # return search_range(self.tree, start, exclusive_end)

def import_classmates(filename):
    """Imports classmates from a tsv file

    Design Recipe step 4 (Templating) is done for you.
    Complete this function by following the template.

    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    tree_map = TreeMap()
    classmates = []
    read_file = open(filename, 'r')
    lines = read_file.readlines()
    read_file.close()
    for line in lines:
        tokens = line.split('\t')
        classmates.append(classmate_factory(tokens))
    for classmate in classmates:
        tree_map.put(classmate.last, classmate)
    return tree_map

def search_classmate(tmap, last):
    """Searches a classmate in a TreeMap using the last name as a key

    Args:
        tmap (TreeMap) : an object of TreeMap
        last (str) : the last name of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the last name does not exist
    """
    if last in tmap:
        return tmap[last]
    else:
        raise KeyError("A classmate with the lastname does not exist!")
