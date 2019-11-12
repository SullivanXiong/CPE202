"""Huffman Coding
CPE202

Author:
    Sullivan Xiong
"""
import sys


class Node:
    """node for huffman node.
    Attributes:
        freq (int) : The frequency of the node
        data (str) : The letter of the node
        left (Node) : The left child Node or None
        right (Node) : The right child Node or None
    """

    def __init__(self, frequency, letter=None, left=None, right=None):
        self.freq = frequency
        self.data = letter
        self.left = left
        self.right = right

    # def __repr__(self):
    #     return "Node({}, {}, {}, {})".format(self.freq, self.data,
    #                                          self.left, self.right)
    def __repr__(self):
        return "Node({}, {})".format(self.freq, self.data)

    def __eq__(self, other):
        return isinstance(other, Node)\
            and self.freq == other.freq\
            and self.data == other.data\
            and self.left == other.left\
            and self.right == other.right


def cnt_freq(filename):
    """returns a Python list of 256 integers the frequencies of characters
    in file
    Args:
        filename (str) : The name of the input file.
    Returns:
        list : A list of size 256 containing the frequencies of the characters
               The indexes refer to the data number of a character.
    """
    res = [0]*256
    with open(filename, "r") as in_file:
        lines = in_file.readlines()
        for line in lines:
            for char in line:
                res[ord(char)] += 1
    return res


def comes_before(node_a, node_b):
    """checks if Node node_a comes before Node node_b.
    Args:
        node_a (Node) : A Node
        node_b (Node) : A Node
    Returns:
        bool : True if node_a has less frequency than node_b, or
               if their frequencies are the same then node_a has
               an ascii of smaller value.
    """
    if node_a.freq == node_b.freq:
        return ord(node_a.data) < ord(node_b.data)
    return node_a.freq < node_b.freq


def create_huff_tree(list_of_freqs):
    """returns the root node of a Huffman Tree
    Args:
    Returns:
    """
    len_freq = len(list_of_freqs)
    node_list = []
    for i in range(len_freq):
        if list_of_freqs[i] > 0:
            insert(node_list, Node(list_of_freqs[i], chr(i)))
    while len(node_list) > 1:
        node_a = dequeue(node_list)
        node_b = dequeue(node_list)
        data = chr(min(ord(node_a.data), ord(node_b.data)))
        frequency_sum = node_b.freq + node_a.freq
        if comes_before(node_a, node_b):
            parent_node = Node(frequency_sum, data, node_a, node_b)
        else:
            parent_node = Node(frequency_sum, data, node_b, node_a)
        insert(node_list, parent_node)
    return node_list[0]


def create_code(root_node, bit=""):
    """returns a Python list of 256 strings representing the code PART B
    Args:
        root_node (Node) : The root node of the huffman tree.
    Returns:
        list : A list of size 256 containing the route required to reach a
               specific character.
    """
    route_list = [""]*256
    if root_node.left is None and root_node.right is None:
        route_list[ord(root_node.data)] += bit
        return route_list
    if root_node.left:
        left_bit = bit + "0"
        left = create_code(root_node.left, left_bit)
        for i in range(256):
            route_list[i] += left[i]
    if root_node.right:
        right_bit = bit + "1"
        right = create_code(root_node.right, right_bit)
        for i in range(256):
            route_list[i] += right[i]
    return route_list


def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    Args:
    Returns:
    """
    huffman_tree = create_huff_tree(cnt_freq(in_file))
    route_list = create_code(huffman_tree)
    with open(in_file, "r") as input_file:
        lines = input_file.readlines()
    with open(out_file, "w") as output_file:
        # output_file.write(header + "\n")
        for line in lines:
            for char in line:
                output_file.write(route_list[ord(char)])


def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """decodes encoded file, writes it to decode file
    Args:
    Returns:
    """
    with open(encoded_file, "r") as input_file:
        lines = input_file.readlines()
    huffman_tree = create_huff_tree(list_of_freqs)
    nxt = huffman_tree
    # for preorder, however we don't need this.
    # header = lines[0]
    # bit_string = lines[1]
    bit_string = lines[0]
    with open(decode_file, "w") as output_file:
        for bit in bit_string:
            if bit == "0":
                nxt = nxt.left
            elif bit == "1":
                nxt = nxt.right
            if nxt.left is None and nxt.right is None:
                output_file.write(nxt.data)
                nxt = huffman_tree


def tree_preord(hufftree):
    """writes a string representation of the Huffman tree
    Args:
    Returns:
    """
    preord = ""
    if hufftree.left is None and hufftree.right is None:
        return "1-{}-".format(ord(hufftree.data))
    preord += "0"
    preord += tree_preord(hufftree.left)
    preord += tree_preord(hufftree.right)
    return preord


def min_heapify(arr):
    """ Turns an array into a min heap
    Args:
    arr (list) : a list of int
    """
    parent = ((len(arr) - 1) - 1) // 2
    while parent >= 0:
        shift_down(arr, parent)
        parent -= 1


def dequeue(arr):
    """pop the minimum valued item from the min heap
    Args:
    arr (list) : a list of int
    Return:
    int : the smallest integer value in the min heap
    Raises:
    IndexError : When the heap is empty or None.
    """
    length = len(arr)
    if arr is None or length == 0:
        raise IndexError('Heap is Empty!')
    if length == 1:
        return arr.pop()
    arr[0], arr[length - 1] = arr[length - 1], arr[0]
    max_item = arr.pop()
    shift_down(arr, 0)
    return max_item


def insert(arr, item):
    """insert a Node into the min heap
    Args:
    arr (list) : a list of int
    item (Node) : the node to be inserted into the min heap
    """
    arr.append(item)
    length = len(arr) - 1
    shift_up(arr, length)


def shift_down(arr, curr):
    """ Shift down an item in the list to keep the min heap order
    Args:
    arr (list) : a list of int
    i (int) : the index of the item of interest
    """
    min_idx = index_minchild(arr, curr)
    if min_idx < 0:
        return
    arr[curr], arr[min_idx] = arr[min_idx], arr[curr]
    shift_down(arr, min_idx)
    return


def shift_up(arr, curr):
    """ Shift up an item in the list to keep the min heap order
    Args:
    arr (list) : a list of int
    i (int) : the index of the item of interest
    """
    parent = (curr - 1) // 2
    if parent >= 0:
        if arr[curr].freq < arr[parent].freq\
            or (arr[curr].freq == arr[parent].freq\
            and arr[curr].data < arr[parent].data):
            arr[curr], arr[parent] = arr[parent], arr[curr]
            shift_up(arr, parent)


def index_minchild(arr, curr):
    """ Computes the index of the child node with a minimum key value
    Args:
    arr (list) : A list of int
    curr (int) : index of the node
    end (int) : the last index of the heap
    Returns:
    int : the index of the child node with minimum key value, or -1 if the
          children are not bigger than the parent or if both children don't
          exist.
    """
    length = len(arr) - 1
    currleft = 2 * curr + 1
    currright = 2 * curr + 2
    left_bool = currleft > length or (arr[curr].freq < arr[currleft].freq\
                 or (arr[curr].freq == arr[currleft].freq\
                 and arr[curr].data < arr[currleft].data))
    right_bool = currright > length or (arr[curr].freq < arr[currright].freq\
                  or (arr[curr].freq == arr[currright].freq\
                  and arr[curr].data < arr[currright].data))
    if left_bool and right_bool:
        return -1
    if currright > length or (arr[currleft].freq < arr[currright].freq\
       or (arr[currleft].freq == arr[currright].freq\
       and arr[currleft].data < arr[currright].data)):
        return currleft
    return currright

def bin_preord(serialized):
    """ converts preorder header into list of bytes
    Args:
        serialized (str) : preorder traverse header
    Returns:
        list : a list of bytes
    """
    list_of_bytes = []
    for int_char in serialized:
        if int_char == "0" or int_char == "1":
            byte = int(int_char, 10).to_bytes(1, byteorder='big')
        else:
            int_char = ord(int_char)
            byte = int_char.to_bytes(1, byteorder='big')
        list_of_bytes.append(byte)
    list_of_bytes.append(255)
    return list_of_bytes

def to_byte_list(char_list):
    """ converts a list of characters into a list of bytes
    Args:
        char_list (list) : a list of one character strings
    Returns:
        list : a list of bytes
    """
    list_of_bytes = []
    for i in range(len(char_list)):
        byte_char = char_list[i]
        byte = int(byte_char, 2).to_bytes(1, byteorder='big')
        list_of_bytes.append(byte)
    return list_of_bytes

def right_zfill(chars, size):
    """ zero pads a string on the right.
    Args:
        chars (list) : a list of characters
        size (int) : size of each 
    Returns:
        list : a list of formatted chars
    """
    for i in range(len(chars)):
        char = '{:<016d}'.format(chars[i])
        chars[i] = char
    return chars

def huffman_encode_bin(in_file, out_file):
    """Encodes a huffman tree in binary
    Args:
        in_file (str) : input file name
        out_file (str) : output file name
    """
    freq_list = cnt_freq(in_file)
    freq_list[3] = 1
    huffman_tree = create_huff_tree(freq_list)
    route_list = create_code(huffman_tree)
    with open(in_file, "r") as input_file:
        lines = input_file.readlines()
    with open(out_file, "w") as output_file:
        # output_file.write(header + "\n")
        output_str = ""
        for line in lines:
            for char in line:
                output_str += route_list[ord(char)]
        output_str += route_list[3]
        output_list = []
        for c in output_str:
            output_list.append(c)
        encoded_binary = to_byte_list(output_list)
        header = bin_preord(tree_preord(huffman_tree))
        for byte in header:
            output_file.write(str(byte))
        output_file.write("\n")
        for byte in encoded_binary:
            output_file.write(str(byte))

def restore_tree(preordstr, tree=None):
    route_list = 256 * [None]
    level = 0
    while preordstr[level] != "-":
        level += 1
    temp_level = level
    flag = None
    first = True
    for i in range(len(preordstr)):
        if preordstr[i] == "-":
            if flag == "-":
                code = ""
                for i in range(temp_level-1):
                    code += "0"
                if first is True:
                    code += "0"
                else:
                    code += "1"
                    temp_level -= 1
                route_list[int(preordstr[ascii_index:i])] = code
                flag = None
            else:
                flag = "-"
                ascii_index = i+1
    first = True
    for i in range(len(route_list)):
        string = route_list[i]
        if string and len(string) == level:
            if first:
                if string[len(string) - 1] == "0":
                    parent_node = Node(1, chr(i))
                    first = False
            else:
                right_node = Node(1, chr(i))
                parent_node = Node(1, parent_node.letter, parent_node, right_node)
                level -= 1
    return parent_node

def convert_bin(num, b):
    """converts an integer to a binary string
    Args:
        num (int) : a number
    Return:
        str : a binary version of the string
    """
    temp_num = num
    binary = 128
    binary_str = ""
    while temp_num > 0 or len(binary_str) < 8:
        if temp_num > 0:
            if temp_num // binary == 1:
                binary_str += "1"
                temp_num -= binary
            else:
                binary_str += "0"
            binary = binary // 2
        else:
            binary_str += "0"
    return binary_str

def get_header_encoded(in_file):
    list_of_bytes = []
    with open(in_file, 'rb') as infile:
        byte = 1
        while byte:
            byte = infile.read(1)
            list_of_bytes.append(byte)
    header_decoded = ""
    for byte in list_of_bytes:
        byte_to_int = int.from_bytes(byte, byteorder=sys.byteorder)
        header_decoded += chr(byte_to_int)
    # print(header_decoded)
    return header_decoded

def huffman_decode_bin(in_file, out_file):
    with open(in_file, "r") as input_file:
        lines = input_file.readlines()
    header_decoded = get_header_encoded(in_file)
    huffman_tree = restore_tree(header_decoded)
    nxt = huffman_tree
    # for preorder, however we don't need this.
    # header = lines[0]
    # bit_string = lines[1]
    bit_string = lines[0]
    with open(out_file, "w") as output_file:
        for bit in bit_string:
            if bit == "0":
                nxt = nxt.left
            elif bit == "1":
                nxt = nxt.right
            if nxt.left is None and nxt.right is None:
                output_file.write(nxt.data)
                nxt = huffman_tree

# huffman_encode("SHA512-Password", "SHA512-Huffman")
# huffman_encode("random.txt", "random-generated")
huffman_decode(cnt_freq("random.txt"), "random-generated-sha512", "password")