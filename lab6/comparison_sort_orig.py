""" Contains the functions for sorting implementation of lab 6
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""
import random
import time

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
        arr[len(arr) - 1 - i], arr[max_idx] = arr[max_idx], arr[len(arr)- 1 - i]
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
                arr[j], arr[j+1] = arr[j+1], arr[j]
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
    for i in range(len(arr)):
        while i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
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
                arr[j], arr[j+1] = arr[j+1], arr[j]
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
    parent = ((len(arr) - 1) - 1 ) // 2
    while parent >= 0:
        shift, comparisons = shift_down(arr, parent, comparisons)
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
    shift, comparisons = shift_down(arr, 0, comparisons, pop_idx - 1)
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
        return None, comparisons
    comparisons += 2
    arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return shift_down(arr, max_idx, comparisons, end), comparisons

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
    if (ileft > end or arr[i] >= arr[ileft])\
    and (iright > end or arr[i] >= arr[iright]):
        return -1, comparisons
    comparisons += 1
    if iright > end or arr[ileft] >= arr[iright]:
        return ileft, comparisons
    return iright, comparisons


random.seed(1) #in order to generate the same sequence of numbers each time.
alist = random.sample(range(5000000), 100000)
blist = random.sample(range(5000000), 100000)
clist = random.sample(range(5000000), 100000)
dlist = random.sample(range(5000000), 100000)
elist = random.sample(range(5000000), 100000)
# Which produce a list of 10 random number between 1 and 10000 [5445, 8692, 6915,
# 8637, 4848, 9408, 1744, 171, 4315, 2949]
# For timing, you can use time class of Python

alist, junk = heap_sort(alist)
blist, junk = heap_sort(blist)
clist, junk = heap_sort(clist)
dlist, junk = heap_sort(dlist)
elist, junk = heap_sort(elist)

start_time = time.time()
result_arr, comparisons = selection_sort(alist)
end_time = time.time()
result_arr2, comparisons2 = bubble_sort(blist)
end_time2 = time.time()
result_arr3, comparisons3 = insertion_sort(clist)
end_time3 = time.time()
result_arr4, comparisons4 = bubble_sort2(dlist)
end_time4 = time.time()
result_arr5, comparisons5 = heap_sort(elist)
end_time5 = time.time()

sort_time = end_time - start_time
sort_time2 = end_time2 - end_time
sort_time3 = end_time3 - end_time2
sort_time4 = end_time4 - end_time3
sort_time5 = end_time5 - end_time4
print("selection sort \t\t {} \t {}".format(comparisons, sort_time))
print("bubble sort \t\t {} \t {}".format(comparisons2, sort_time2))
print("insertion sort \t\t {} \t {}".format(comparisons3, sort_time3))
print("bubble sort 2 \t\t {} \t {}".format(comparisons4, sort_time4))
print("heap sort \t\t {} \t\t {}".format(comparisons5, sort_time5))

f = open("comparison_sorted_500000", "w")
f.write("selection sort \t\t {} \t {}\n".format(comparisons, sort_time))
f.write("bubble sort \t\t {} \t {}\n".format(comparisons2, sort_time2))
f.write("insertion sort \t\t {} \t {}\n".format(comparisons3, sort_time3))
f.write("bubble sort 2 \t\t {} \t {}\n".format(comparisons4, sort_time4))
f.write("heap sort \t\t\t {} \t\t {}\n".format(comparisons5, sort_time5))
f.close()
