""" Contains Binary Seach Tree implementation.
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""


class BSTNode:
    """ Node for Binary Search Tree
    Attributes:
        data (int): payload of the node
        left (BSTNode): left subtree of BinarySearchTree
        right (BSTNode): right subtree of BinarySearchTree
    """

    def __init__(self, key, data, color=None, left=None, right=None):
        self.key = key
        self.data = data
        self.color = color
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, type(self))\
            and self.data == other.data\
            and self.left == other.left\
            and self.right == other.right

    # def __repr__(self):
    #     return "BSTNode(key: {}, data: {}, left: {}, right: {})".format(
    #         self.key, self.data, self.left, self.right)

    def __repr__(self):
        return "BSTNode(key: {}, color: {}, left: {}, right: {})".format(self.key, self.color, self.left, self.right)


def get(tree, key):
    """Gets the node with the respective key if it exists.
    Args:
        tree (BSTNode): A binary search tree.
        key (string): The last name that we are searching for.
    Returns:
        BSTNode: The binary search tree with the corresponding key if
                 it exists, otherwise None.
    """
    if tree is None:
        return None
    if tree.key == key:
        return tree
    if tree.key > key:
        return get(tree.left, key)
    if tree.key < key:
        return get(tree.right, key)


def contains(tree, key):
    """Checks to see if the tree has a node with the corresponding key.
    Args:
        tree (BSTNode): A binary search tree.
        key (string): The last name that we are searching for.
    Returns:
        boolean: True if the tree does have a node with the corresponding key,
                 else False if it doesn't exist.
    """
    if get(tree, key):
        return True
    return False


def insert(tree, key, data):
    """Insert a classmate into the tree.
    If the key already exists, replace the key's data with the new data.
    Args:
        tree (BSTNode): A binary search tree.
        key (string): The last name of the classmate we are inserting to the
                      tree.
        data (Classmate): The classmate that we are inserting into the tree
    Returns:
        BSTNode: The root node of the binary search tree if the corresponding
                 key exists, otherwise None.
    """
    tree = insert_helper(tree, key, data)
    return BSTNode(tree.key, tree.data, "B", tree.left, tree.right)

def insert_helper(tree, key, data):
    """a helper function for inserting a node to
    a Float Red Black Tree
    inserts a value to the tree to construct a BST recursively
    Args:
        tree (RBTreeFloatNode): a bst node
        data (MaybeFloat):
    Returns:
        RBTreeFloatNode : a Float Red Black Tree
    """
    if tree is None:  # base case
        return BSTNode(key, data, "R", None, None)
    else:
        if key < tree.key:
            return rebalance(
                BSTNode(
                    tree.key, tree.data, tree.color,
                    insert_helper(tree.left, key, data), tree.right))
        else:
            return rebalance(
                BSTNode(
                    tree.key, tree.data, tree.color,
                    tree.left, insert_helper(tree.right, key, data)))

def rebalance(tree):
    """Rebalance the tree so that the property of the RB Tree is maintained.
    If the subtree matches one of the 4 patterns, it will convert the subtree to
    BRB
    Args:
        tree (BSTNode): a Float Red Black Tree
    Returns:
        BSTNode : a Float Red Black Tree
    """
    #RRB pattern
    if tree.color == 'B' and tree.left and tree.left.color == 'R'\
        and tree.left.left and tree.left.left.color == 'R':
        #convert to BRB
        return BSTNode(
        tree.left.key, tree.left.data, "R",
        BSTNode(
        tree.left.left.key, tree.left.left.data, "B",
        tree.left.left.left,
        tree.left.left.right),
        BSTNode(
        tree.key, tree.data, "B",
        tree.left.right,
        tree.right))
    #R RB pattern
    elif tree.color == 'B' and tree.left and tree.left.color == 'R'\
        and tree.left.right and tree.left.right.color == 'R':
        #convert to BRB
        return BSTNode(
        tree.left.right.key, tree.left.right.data, 'R',
        BSTNode(
        tree.left.key, tree.left.data, 'B',
        tree.left.left,
        tree.left.right.left),
        BSTNode(
        tree.key, tree.data, 'B',
        tree.left.right.right,
        tree.right))
    #BR R pattern
    elif tree.color == 'B' and tree.right and tree.right.color == 'R'\
        and tree.right.left and tree.right.left.color == 'R':
        #convert to BRB
        return BSTNode(
        tree.right.left.key, tree.right.left.data, "R",
        BSTNode(
        tree.key, tree.data, 'B',
        tree.left,
        tree.right.left.left),
        BSTNode(
        tree.right.key, tree.right.data, 'B',
        tree.right.left.right,
        tree.right.right))
    #one more elif to convert BRR pattern to BRB
    elif tree.color == 'B' and tree.right and tree.right.color == 'R'\
        and tree.right.right and tree.right.right.color == 'R':
        return BSTNode(
        tree.right.key, tree.right.data, "R",
        BSTNode(
        tree.key, tree.data, 'B',
        tree.left,
        tree.right.left),
        BSTNode(
        tree.right.right.key, tree.right.right.data, 'B',
        tree.right.right.left,
        tree.right.right.right))
    if tree.left and tree.left.left is None\
        and tree.left.right is None:
        return BSTNode(
        tree.key, tree.data, tree.color,
        BSTNode(
        tree.left.key, tree.left.data, tree.left.color,
        tree.left.left, tree.left.right
        ), tree.right)
    elif tree.right and tree.right.left is None\
        and tree.right.right is None:
        return BSTNode(
        tree.key, tree.data, tree.color, tree.left,
        BSTNode(
        tree.right.key, tree.right.data, tree.right.color,
        tree.right.left, tree.right.right
        ))
    return tree


def delete(tree, key):
    """Removes the node with the corresponding key from the Tree if it exists.
    Args:
        tree (BSTNode): A binary search tree.
        key (string): The last name of the classmate that we are removing from
                      the tree.
    Returns:
        BSTNode: The root node of the binary search tree if the corresponding
                 key exists, otherwise None.
    """
    if tree is None:
        return None
    if tree.key == key:
        if tree.left is None and tree.right is None:
            return None
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left
        replacement = get_replacement(tree.right, tree)
        replacement.left = tree.left
        if tree.right != replacement:
            replacement.right = tree.right
        return replacement
    if tree.key > key:
        tree.left = delete(tree.left, key)
    if tree.key < key:
        tree.right = delete(tree.right, key)
    return tree


def get_replacement(current, parent):
    """A helper function to get a replacement node the delete function.
    Args:
        current (BSTNode): current node
        parent (BSTNode): parent node
    Returns:
        BSTNode: a replacement node
    """
    if current.left is None:
        if current.right is None:
            if current == parent.left:
                parent.left = None
            else:
                parent.right = None
            return current
        if current == parent.left:
            parent.left = current.right
        else:
            parent.right = current.right
        current.right = None
        return current
    return get_replacement(current.left, current)


def size(tree):
    """Returns the number of nodes in the tree.
    Args:
        tree (BSTNode): A binary search tree.
    Returns:
        int: The number of nodes in the binary search tree.
    """
    if tree is None:
        return 0
    return 1 + size(tree.left) + size(tree.right)


def find_min(tree):
    """Finds the minimum node in the tree.
    Args:
        tree (BSTNode): A binary search tree.
    Returns:
        BSTNode: The minimum node in the tree.
    """
    if tree is None:
        return None
    elif tree.left is None:
        return tree
    return find_min(tree.left)


def find_max(tree):
    """Finds the maximum node in the tree.
    Args:
        tree (BSTNode): A binary search tree.
    Returns:
        BSTNode: The maximum node in the tree.
    """
    if tree is None:
        return None
    elif tree.right is None:
        return tree
    return find_max(tree.right)


def inorder_list(tree):
    """Returns a list of the tree in in-order traversal order.
    Args:
        tree (BSTNode): A binary search tree.
    Returns:
        list: A list containing the tree's nodes in in-order traversal order.
    """
    if tree is None:
        return []
    if tree.left is None and tree.right is None:
        return [tree.key]
    lst = []
    lst += inorder_list(tree.left)
    lst.append(tree)
    lst += inorder_list(tree.right)
    return lst


def preorder_list(tree):
    """Returns a list of the tree in pre-order traversal order.
    Args:
        tree (BSTNode): A binary search tree.
    Returns:
        list: A list containing the tree's nodes in pre-order traversal order.
    """
    if tree is None:
        return []
    if tree.left is None and tree.right is None:
        return [tree.key]
    lst = [tree.key]
    lst += preorder_list(tree.left)
    lst += preorder_list(tree.right)
    return lst


def tree_height(tree):
    """Returns the height of the tree.
    Args:
        tree (BSTNode): A binary search tree.
    Returns:
        int: The height of the tree.
    """
    if tree is None:
        return 0
    left = 0
    right = 0
    if tree.left:
        left += 1 + tree_height(tree.left)
    if tree.right:
        right += 1 + tree_height(tree.right)
    if left >= right:
        return left
    return right


# def search_range(tree, start, end):
#     res = []
#     left = []
#     right = []
#     tree and tree.left.key[0] >= start and tree.left.key[0] < end:
#         left += search_range(tree.left, start, end)
#     tree and tree.right.key[0] >= start and tree.right.key[0] < end:
#         right += search_range(tree.right, start, end)
#     res += left
#     tree and tree.key[0] >= start and tree.key[0] < end:
#         res.append(tree)
#     res += right
#     return res
