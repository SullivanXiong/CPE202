""" Contains solutions for lab2
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""

#1
def perm_lex(string):
    """ Use a recursive solution to get all possible permutations of a given
        string in lexigraphical order.

    Args:
        string(str): The string that will used to find all permutations in
                    lexicographic order.

    Returns:
        list: List of permutations in lexicographic order.
    """
    if string == None or len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        list_of_perms = []
        for i, char in enumerate(string):
            current = char
            left_and_right = string[:i] + string[i + 1:]
            for j in perm_lex(left_and_right):
                list_of_perms.append(current + j)
        return list_of_perms
