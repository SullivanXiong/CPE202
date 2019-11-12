""" Contains the functions for sorting implementation of lab 6
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""
import random
import time

def quick_sort_helper(array, start, end, count):
    """quick sort algorithm helper function- Meha Sharma
    Args:
        array: list to be sorted
        start: starting index
        end: end index
        count: count of comparisons
    Returns:
        list: sorted list
        int: count of comparisons"""
    if start <= end:
        count += 1
        pivot = array[(end + start) // 2]
        array[start], array[(end + start) // 2] = array[(end + start) // 2], array[start]
        left = start + 1
        right = end
        while left <= right:
            count += 1
            if array[left] > pivot and array[right] < pivot:
                count += 1
                array[left], array[right] = array[right], array[left]
            if array[left] < pivot:
                count += 1
                left = left + 1
            if array[right] > pivot:
                count += 1
                right = right - 1
        array[start], array[right] = array[right], array[start]
        quick_sort_helper(array, start, right - 1, count)
        quick_sort_helper(array, right + 1, end, count)
    return array, count


def quick_sort(a_list):
    """quick sort algorithm -Meha Sharma
    Args:
        a_list: list to be sorted
    Returns:
        list: sorted list
        int: count of comparisons"""
    ans, count = quick_sort_helper(a_list, 0, len(a_list) - 1, 0)
    return ans, count


def merge_sort(a_list, count):
    """merge sort algorithm- Meha Sharma
    Args:
        a_list: list to be sorted
        count: count of comparisons
    Returns:
        list: sorted list
        int: count of comparisons"""
    if len(a_list) <= 1:
        return a_list, count
    mid_point = len(a_list) // 2
    left = a_list[:mid_point]
    right = a_list[mid_point:]
    left_ans, count = merge_sort(left, count)
    right_ans, count = merge_sort(right, count)
    ans, count = merge(left_ans, right_ans, count)
    return ans, count


def merge(left, right, count):
    """merge sort algorithm helper function- Meha Sharma
    Args:
        left: left side of array to be sorted
        right: left side of array to be sorted
        count: count of comparisons
    Returns:
        list: sorted list
        int: count of comparisons"""
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            count += 1
            merged.append(left[i])
            i += 1
        elif right[j] < left[i]:
            count += 1
            merged.append(right[j])
            j += 1
    while i < len(left):
        count += 1
        merged.append(left[i])
        i += 1
    while j < len(right):
        count += 1
        merged.append(right[j])
        j += 1
    return merged, count


def selection_sort(arr):
    """ Sorting algorithm using the selection sort solution
    Written by: Sullivan Xiong
    Args:
        arr (list) : A randomly sorted list of ints
    returns:
        list : ascending sorted list of ints
        comparisons : the number of comparisons to sort the list.
    """
    comparisons = 0
    for i in range(len(arr) - 1):
        max_idx = 0
        for j in range(1, len(arr) - i):
            comparisons += 1
            if arr[max_idx] <= arr[j]:
                max_idx = j
        arr[len(arr) - 1 - i], arr[max_idx] = arr[max_idx], arr[len(arr) - 1 - i]
    return arr, comparisons


def bubble_sort(arr):
    """ Sorting algorithm using the bubble sort solution
    Written by: Sullivan Xiong
    Args:
        arr (list) : A randomly sorted list of ints
    returns:
        list : ascending sorted list of ints
        comparisons : the number of comparisons to sort the list.
    """
    comparisons = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparisons


def insertion_sort(arr):
    """ Sorting algorithm using the insertion sort solution
    Written by: Sullivan Xiong
    Args:
        arr (list) : A randomly sorted list of ints
    returns:
        list : ascending sorted list of ints
        comparisons : the number of comparisons to sort the list.
    """
    comparisons = 0
    length = len(arr)
    for i in range(length):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            comparisons += 1
        comparisons += 1
    return arr, comparisons


def bubble_sort2(arr):
    """ Sorting algorithm using the selection sort solution
    Written by: Sullivan Xiong
    Args:
        arr (list) : A randomly sorted list of ints
    returns:
        list : ascending sorted list of ints
        comparisons : the number of comparisons to sort the list.
    """
    comparisons = 0
    swapped = False
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr, comparisons
    return arr, comparisons


def heap_sort(arr):
    """ Sorting algorithm using the heap sort solution
    Written by: Sullivan Xiong
    Args:
        arr (list) : A randomly sorted list of ints
    returns:
        list : ascending sorted list of ints
        comparisons : the number of comparisons to sort the list.
    """
    comparisons = 0
    comparisons = max_heapify(arr, comparisons)
    for i in range(len(arr) - 1):
        comparisons = dequeue(arr, len(arr) - 1 - i, comparisons)
    return arr, comparisons


def max_heapify(arr, comparisons):
    """ Turns an array into a max heap
    Args:
    arr (list) : a list of int
    """
    parent = ((len(arr) - 1) - 1) // 2
    while parent >= 0:
        comparisons = shift_down(arr, parent, comparisons)
        parent -= 1
    return comparisons


def dequeue(arr, pop_idx, comparisons):
    """pop the minimum valued item from the min heap
    Args:
    arr (list) : a list of int
    Return:
    int : the smallest integer value in the min heap
    Raises:
    IndexError : When the heap is empty or None.
    """
    if arr is None or len(arr) == 0:
        raise IndexError('Heap is Empty!')
    if len(arr) == 1:
        return arr.pop()
    comparisons += 2
    max_item = arr[0]
    last_item = arr[pop_idx]
    arr[0] = last_item
    arr[pop_idx] = max_item
    comparisons = shift_down(arr, 0, comparisons, pop_idx - 1)
    return comparisons


def shift_down(arr, i, comparisons, end=None):
    """ Shift down an item in the list to keep the max heap order
    Args:
    arr (list) : a list of int
    i (int) : the index of the item of interest
    """
    length = len(arr)
    if end is None:
        end = length - 1
    max_idx, comparisons = index_maxchild(arr, i, end, comparisons)
    if max_idx < 0:
        return comparisons
    comparisons += 2
    arr[i], arr[max_idx] = arr[max_idx], arr[i]
    shift_down(arr, max_idx, comparisons, end)
    return comparisons


def index_maxchild(arr, i, end, comparisons):
    """ Computes the index of the child node with a maximum key value
    Args:
    arr (list) : A list of int
    i (int) : index of the node
    end (int) : the last index of the heap
    Returns:
    int : the index of the child node with minimum key value, or -1 if the
          children are not bigger than the parent or if both children don't
          exist.
    """
    ileft = 2 * i + 1
    iright = 2 * i + 2
    comparisons += 2
    if (ileft > end or arr[i] >= arr[ileft]) \
            and (iright > end or arr[i] >= arr[iright]):
        return -1, comparisons
    comparisons += 1
    if iright > end or arr[ileft] >= arr[iright]:
        return ileft, comparisons
    return iright, comparisons
