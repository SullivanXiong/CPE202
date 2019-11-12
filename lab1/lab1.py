""" Contains solutions for lab1
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""

import unittest

# 1


def get_max(int_list):
    """ Uses an interative solution to get the maximum in a list of integers.
        If the list if empty then return None instead.

    Args:
        int_list(list): A list of integers.

    Returns:
        int: Returns the maximum integer.
    """
    if len(int_list) == 0:
        return None
    maximum = 0
    for i in range(1, len(int_list)):
        if int_list[i] > int_list[maximum]:
            maximum = i
    return int_list[maximum]

# 2


def reverse(string):
    """ Uses a recursive solution to reverse a string.

    Args:
        string(str): The string to be reversed.

    Returns:
        str: The reversed version of string.
    """
    if len(string) == 0:
        return ""
    return reverse_helper(string, len(string) - 1)


def reverse_helper(string, current):
    """ Helper function for the function reverse.

    Args:
        string(str): The string to be reversed.
        current(int): The current index being accessed.

    Returns:
        str: The reversed version of string
    """
    if current == 0:
        return string[current]
    return string[current] + reverse_helper(string, current - 1)

# 3


def search(int_list, target):
    """ Uses a recursive solution to implement binary search. Searchs a list
        of integers and returns the index of the target if it exist. If the
        list is empty or the target is not found, returns None.

    Args:
        int_list(list): A sorted list of integers.
        target(int): The target we are searching for in int_list.

    Returns:
        int: The index of the target
    """
    if len(int_list) == 0:
        return None
    return search_helper(int_list, target, 0, len(int_list) - 1)


def search_helper(int_list, target, start, end):
    """ Helper function for the function search.

    Args:
        int_list(list): A sorted list of integers.
        target(int): The target we are searching for in int_list.
        start: The starting index of the int_list.
        end: The last index of the int_list.

    Returns:
        int: The index of the target
    """
    middle = (start + end) // 2
    if int_list[middle] == target:
        return middle
    elif start == end:
        return None
    elif int_list[middle] < target:
        return search_helper(int_list, target, middle + 1, end)
    elif int_list[middle] > target:
        return search_helper(int_list, target, start, middle - 1)

# 4


def fib(num):
    """ Uses a recursive solution to compute the nth Fibonacci number.

    Args:
        num(integer): The nth number that is wanted from Fibonacci
                    sequence.

    Returns:
        int: Returns the number at the nth position of the Fibonacci
                sequence.
    """
    fib_list = [None] * (num + 1)
    return fib_helper(num, fib_list)


def fib_helper(num, fib_list):
    """ Helper function for the function fib.

    Args:
        num(integer): The nth number that is wanted from Fibonacci
                    sequence.
        fib_list(list): The list that keeps track of what has been seen
                        already.

    Returns:
        int: Returns the number at the nth position of the Fibonacci
                sequence.
    """
    if fib_list[num] != None:
        return fib_list[num]
    elif num == 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        result = fib_helper(num - 1, fib_list) + fib_helper(num - 2, fib_list)
    fib_list[num] = result
    return result

# 5.1 factorial iterative version


def factorial_iter(num):
    """ Uses an iterative solution to compute the nth factorial.

    Args:
        num(int): The nth number of a factorial.

    Returns:
        int: The value at that nth factorial.
    """
    if num == 0 or num == 1:
        return 1
    i = 2
    result = 1
    while i <= num:
        result = result * i
        i += 1
    return result

# 5.2 factorial recursive version


def factorial_rec(num):
    """ Uses a recursive solution to compute the nth factorial.

    Args:
        num(int): The nth number of a factorial.

    Returns:
        int: The value at that nth factorial.
    """
    fac_list = [None] * (num + 1)
    return factorial_rec_helper(num, fac_list)


def factorial_rec_helper(num, fac_list):
    """ Uses a recursive solution to compute the nth factorial.

    Args:
        num(int): The nth number of a factorial.
        fac_list(list): list that keeps track of the factorials that have
                        been seen already.

    Returns:
        int: The value at that nth factorial.
    """
    if fac_list[num] != None:
        return fac_list[num]
    elif num == 0 or num == 1:
        return 1
    else:
        fac_list[num] = num * factorial_rec_helper(num - 1, fac_list)
    return fac_list[num]


def main():
    """ lines of code written in this main function will be executed
    when you execute this file in a standalone fashion.
    you can test your fucntions here as well.
    """
    unittest.main()


if __name__ == '__main__':
    main()
